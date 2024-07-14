<template>
    <div class="flex">
        <!-- Main form covering 3/4 of the page -->
        <div class="w-3/4 p-4 bg-white shadow-md rounded-md relative">
            <!-- Breadcrumb navigation -->
            <nav aria-label="breadcrumb" class="w-max">
                <ol
                    class="flex flex-wrap items-center w-full bg-opacity-60 rounded-md bg-transparent p-0 transition-all">
                    <li
                        class="flex items-center text-blue-gray-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-light-blue-500">
                        <nuxt-link to="/purchase">
                            <p
                                class="block antialiased font-sans text-sm leading-normal text-blue-900 font-normal opacity-50 transition-all hover:text-blue-500 hover:opacity-100">
                                dashboard
                            </p>
                        </nuxt-link>
                        <span
                            class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
                    </li>
                    <li
                        class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                        <nuxt-link to="/purchase/orders/">
                            <p
                                class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                                Orders
                            </p>
                        </nuxt-link>
                        <span
                            class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
                    </li>
                    <li
                        class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                        <nuxt-link to="/purchase/orders/po">
                            <p
                                class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                                Purchase Order
                            </p>
                        </nuxt-link>
                        <span
                            class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
                    </li>
                    <li
                        class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                        <nuxt-link to="/purchase/orders/vendors/newpo">
                            <p
                                class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                                New Purchase Order
                            </p>
                        </nuxt-link>
                    </li>
                </ol>
            </nav>

            <!-- Buttons for actions -->
            <div class="mt-6 flex space-x-4">
                <button type="button" @click="openModal('create')"
                    class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">Create
                    Purchase Order</button>
                <button type="button" @click="openModal('send')"
                    class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">Send
                    By Email</button>
                <button type="button" @click="openModal('download')"
                    class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">Download
                    Purchase Order</button>
            </div>

            <!-- Form for PO details -->
            <div class="p-4 bg-card text-card-foreground relative">
                <form @submit.prevent="submitForm" class="space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="company-name" class="block text-sm font-medium text-muted-foreground">Company
                                Name</label>
                            <select v-model="rfq.vendor_reference" id="company-name"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground">
                                <option value="">Select Company</option>
                                <option v-for="company in companyOptions" :key="company" :value="company">{{ companyName
                                    }}</option>
                            </select>
                        </div>
                        <div>
                            <label for="company-name" class="block text-sm font-medium text-muted-foreground">Vendor
                                Name</label>
                            <select v-model="rfq.vendor_reference" id="company-name"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground">
                                <option value="">Select Company</option>
                                <option v-for="company in companyOptions" :key="company" :value="company">{{ vendor.name
                                    }}</option>
                            </select>
                        </div>
                        <div>
                            <label for="currency"
                                class="block text-sm font-medium text-muted-foreground">Currency</label>
                            <input v-model="po.currency" type="text" id="currency"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                        </div>
                        <div>
                            <label for="order-deadline" class="block text-sm font-medium text-muted-foreground">Order
                                Deadline</label>
                            <input v-model="rfq.order_deadline" type="date" id="order-deadline"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                        </div>
                        <div>
                            <label for="expected-arrival"
                                class="block text-sm font-medium text-muted-foreground">Expected Arrival</label>
                            <input v-model="rfq.expected_arrival" type="date" id="expected-arrival"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                        </div>
                        <div>
                            <label for="confirmation-date"
                                class="block text-sm font-medium text-muted-foreground">Confirmation Date</label>
                            <input v-model="rfq.confirmation_date" type="date" id="confirmation-date"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                        </div>
                        <div>
                            <label for="source-document" class="block text-sm font-medium text-muted-foreground">Source
                                Document</label>
                            <input v-model="rfq.source_document" type="text" id="source-document"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                        </div>
                        <div>
                            <label for="vendor-id" class="block text-sm font-medium text-muted-foreground">Vendor
                                ID</label>
                            <input v-model="rfq.vendor_id" type="text" id="vendor-id"
                                class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                        </div>
                    </div>
                    <div>
                        <label for="deliver-to" class="block text-sm font-medium text-muted-foreground">Deliver
                            To</label>
                        <input v-model="rfq.deliver_to" type="text" id="deliver-to"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                    </div>

                    <!-- Products list -->
                    <div class="mt-6">
                        <h3 class="text-lg font-medium text-muted-foreground">Products</h3>
                        <div id="products-list" class="grid grid-cols-1 gap-4 mt-2 overflow-x-auto">
                            <div class="flex flex-wrap">
                                <div v-for="(product, index) in rfq.products" :key="index"
                                    class="product-entry flex items-start space-x-4">
                                    <div class="flex flex-col">
                                        <label for="product"
                                            class="block text-sm font-medium text-muted-foreground">Product</label>
                                        <select v-model="product.product_id"
                                            class="product-select mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground">
                                            <option>Select Product</option>
                                            <option v-for="(option, index) in productOptions" :key="index"
                                                :value="index + 1">{{ option }}</option>
                                        </select>
                                    </div>
                                    <div class="flex flex-col">
                                        <label for="quantity"
                                            class="block text-sm font-medium text-muted-foreground">Quantity</label>
                                        <input v-model="product.quantity" type="number"
                                            class="quantity-input mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                            @input="updatePrice(index)" />
                                    </div>
                                    <div class="flex flex-col">
                                        <label for="unit-price"
                                            class="block text-sm font-medium text-muted-foreground">Unit Price</label>
                                        <input v-model="product.unit_price" type="number"
                                            class="unit-price-input mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                            @input="updatePrice(index)" />
                                    </div>
                                    <div class="flex flex-col">
                                        <label for="subtotal"
                                            class="block text-sm font-medium text-muted-foreground">Subtotal</label>
                                        <input v-model="product.subtotal" type="number"
                                            class="subtotal-input mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                            disabled />
                                    </div>
                                    <button type="button" class="mt-6 text-red-500"
                                        @click="removeProduct(index)">Remove</button>
                                </div>
                            </div>
                        </div>
                        <button type="button" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                            @click="addProduct">Add Product</button>
                    </div>

                    <div class="mt-6">
                        <button type="submit"
                            class="w-full px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600">Submit
                            Purchase Order</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Log section covering 1/4 of the page -->
        <div class="w-1/4 p-4 bg-gray-200 text-gray-900 shadow-md rounded-md">
            <h2 class="text-lg font-semibold mb-4">Log</h2>
            <div v-for="log in logs" :key="log.id" class="log-entry mb-2 p-2 bg-white rounded shadow-sm">
                {{ log.message }}
            </div>
        </div>
    </div>

    <!-- Modal for confirming actions -->
    <confirm-modal v-if="showModal" :action="modalAction" @confirm="handleConfirm" @cancel="showModal = false" />
</template>
<script setup>
import { ref } from 'vue';


const rfq = ref({
  vendor_reference: '',
  currency: '',
  order_deadline: '',
  expected_arrival: '',
  confirmation_date: '',
  source_document: '',
  vendor_id: '',
  deliver_to: '',
  products: [],
});

const companyOptions = ref(['Company A', 'Company B', 'Company C']);
const productOptions = ref(['Product 1', 'Product 2', 'Product 3']);
const logs = ref([]);
const showModal = ref(false);
const modalAction = ref('');

const openModal = (action) => {
  modalAction.value = action;
  showModal.value = true;
};

const handleConfirm = () => {
  if (modalAction.value === 'create') {
    createPurchaseOrder();
  } else if (modalAction.value === 'send') {
    sendPurchaseOrder();
  } else if (modalAction.value === 'download') {
    downloadPurchaseOrder();
  }
  showModal.value = false;
};

const createPurchaseOrder = () => {
  logs.value.push({ id: logs.value.length + 1, message: 'Purchase Order Created' });
};

const sendPurchaseOrder = () => {
  logs.value.push({ id: logs.value.length + 1, message: 'Purchase Order Sent by Email' });
};

const downloadPurchaseOrder = () => {
  logs.value.push({ id: logs.value.length + 1, message: 'Purchase Order Downloaded' });
};

const addProduct = () => {
  rfq.value.products.push({ product_id: '', quantity: '', unit_price: '', subtotal: '' });
};

const removeProduct = (index) => {
  rfq.value.products.splice(index, 1);
};

const updatePrice = (index) => {
  const product = rfq.value.products[index];
  product.subtotal = product.quantity * product.unit_price;
};

const submitForm = () => {
  console.log('Form submitted', rfq.value);
};
</script>
<style scoped>
.log-entry {
  max-height: 150px;
  overflow-y: auto;
}
.product-entry {
  gap: 1rem;
}
</style>
