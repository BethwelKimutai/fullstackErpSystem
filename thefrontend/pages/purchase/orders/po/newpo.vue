<template>
    <div class="p-4 max-w-4xl mx-auto bg-white shadow-md rounded-md relative">
        <nav aria-label="breadcrumb" class="w-max">
            <ol class="flex flex-wrap items-center w-full bg-opacity-60 rounded-md bg-transparent p-0 transition-all">
                <li
                    class="flex items-center text-blue-gray-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-light-blue-500">
                    <nuxt-link to="/purchase">
                        <p
                            class="block antialiased font-sans text-sm leading-normal text-blue-900 font-normal opacity-50 transition-all hover:text-blue-500 hover:opacity-100">
                            dashboard</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            Orders</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>

                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/po">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            Purchase Order</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>

                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/vendors/newpo">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            New Purchase Order</p>
                    </nuxt-link>

                </li>
            </ol>
        </nav>
        <!-- Buttons for actions -->
        <div class="mt-6 flex space-x-4">
            <button type="button" @click="openModal('create')"
                class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Create Purchase Order
            </button>
            <button type="button" @click="openModal('send')"
                class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Send By Email
            </button>
            <button type="button" @click="openModal('download')"
                class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Download Purchase Order
            </button>
        </div>

        <!-- Form for PO details -->
        <div class="p-4 bg-card text-card-foreground relative">
            <form @submit.prevent="submitForm" class="space-y-4">
                <!-- Vendor Reference, Currency, Order Deadline, Expected Arrival, Deliver To, and Products -->
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label for="company-name" class="block text-sm font-medium text-muted-foreground">Company Name</label>
                        <select v-model="rfq.vendor_reference" id="company-name"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground">
                            <option value="">Select Company</option>
                            <option v-for="company in companyOptions" :key="company" :value="company">{{ companyName }}</option>
                        </select>
                    </div>
                    <div>
                        <label for="company-name" class="block text-sm font-medium text-muted-foreground">Vendor Name</label>
                        <select v-model="rfq.vendor_reference" id="company-name"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground">
                            <option value="">Select Company</option>
                            <option v-for="company in companyOptions" :key="company" :value="company">{{ vendor.name }}</option>
                        </select>
                    </div>

                    <div>
                        <label for="currency" class="block text-sm font-medium text-muted-foreground">Currency</label>
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
                        <label for="expected-arrival" class="block text-sm font-medium text-muted-foreground">Expected
                            Arrival</label>
                        <input v-model="rfq.expected_arrival" type="date" id="expected-arrival"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                    </div>
                    <div class="mt-6">
                        <label for="confirmation-date"
                            class="block text-sm font-medium text-muted-foreground">Confirmation Date</label>
                        <input v-model="rfq.confirmation_date" type="date" id="confirmation-date"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                    </div>
                    <div class="mt-6">
                        <label for="source-document" class="block text-sm font-medium text-muted-foreground">Source
                            Document</label>
                        <input v-model="rfq.source_document" type="text" id="source-document"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                    </div>
                    <div class="mt-6">
                        <label for="vendor-id" class="block text-sm font-medium text-muted-foreground">Vendor ID</label>
                        <input v-model="rfq.vendor_id" type="text" id="vendor-id"
                            class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" />
                    </div>
                </div>
                <div>
                    <label for="deliver-to" class="block text-sm font-medium text-muted-foreground">Deliver To</label>
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
                                    <label for="unit-price" class="block text-sm font-medium text-muted-foreground">Unit
                                        Price</label>
                                    <input v-model="product.unit_price" type="number"
                                        class="unit-price-input mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                        @input="updatePrice(index)" />
                                </div>
                                <div class="flex flex-col">
                                    <label for="taxes"
                                        class="block text-sm font-medium text-muted-foreground">Taxes</label>
                                    <input v-model="product.taxes" type="number" id="taxes"
                                        class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                        @input="updatePrice(index)" />
                                </div>
                                <div class="flex flex-col">
                                    <label for="tax-excluded"
                                        class="block text-sm font-medium text-muted-foreground">Tax Excluded</label>
                                    <input v-model="product.tax_excluded" type="number" id="tax-excluded"
                                        class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                        disabled />
                                </div>
                                <div class="flex flex-col">
                                    <label for="subtotal"
                                        class="block text-sm font-medium text-muted-foreground">Subtotal</label>
                                    <input v-model="product.subtotal" type="number" id="subtotal"
                                        class="mt-1 block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground"
                                        disabled />
                                </div>
                                <button type="button" @click="removeProduct(index)"
                                    class="mt-6 px-2 py-1 bg-red-500 text-white rounded-md shadow-sm hover:bg-red-700">Remove</button>
                            </div>
                        </div>
                    </div>
                    <button type="button" @click="addProduct"
                        class="mt-4 px-4 py-2 bg-green-500 text-white rounded-md shadow-sm hover:bg-green-700">Add
                        Product</button>
                </div>

                <!-- Total amounts -->
                <div class="mt-6">
                    <div class="flex justify-between">
                        <span class="text-sm font-medium text-muted-foreground">Total Tax Excluded:</span>
                        <span class="text-sm font-medium text-muted-foreground">{{ totalTaxExcluded }}</span>
                    </div>
                    <div class="flex justify-between mt-2">
                        <span class="text-sm font-medium text-muted-foreground">Total Taxes:</span>
                        <span class="text-sm font-medium text-muted-foreground">{{ totalTaxes }}</span>
                    </div>
                    <div class="flex justify-between mt-2">
                        <span class="text-sm font-medium text-muted-foreground">Total:</span>
                        <span class="text-sm font-medium text-muted-foreground">{{ total }}</span>
                    </div>
                </div>
                <div class="mt-6">
                    <button type="submit"
                        class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                        Submit
                    </button>
                </div>
            </form>
        </div>

        <!-- Modal for confirmation -->
        <modal v-if="showModal" @close="showModal = false">
            <div class="bg-card text-card-foreground relative rounded-md p-6">
                <h3 class="text-lg font-medium mb-4">Confirm Action</h3>
                <p class="mb-4">Are you sure you want to {{ modalAction }}?</p>
                <div class="flex justify-end space-x-2">
                    <button @click="showModal = false"
                        class="px-4 py-2 bg-red-500 text-white rounded-md shadow-sm hover:bg-red-700">Cancel</button>
                    <button @click="confirmAction"
                        class="px-4 py-2 bg-green-500 text-white rounded-md shadow-sm hover:bg-green-700">Confirm</button>
                </div>
            </div>
        </modal>

        <!-- Modal for success message -->
        <modal v-if="showSuccessModal" @close="showSuccessModal = false">
            <div class="bg-card text-card-foreground relative rounded-md p-6">
                <h3 class="text-lg font-medium mb-4">Action Successful</h3>
                <p class="mb-4">Your action has been completed successfully.</p>
                <div class="flex justify-end">
                    <button @click="showSuccessModal = false"
                        class="px-4 py-2 bg-green-500 text-white rounded-md shadow-sm hover:bg-green-700">OK</button>
                </div>
            </div>
        </modal>
    </div>
</template>

<script>
import { ref, reactive, computed } from 'vue';

export default {
    components: {
        Modal
    },
    setup() {
        const rfq = reactive({
            vendor_reference: '',
            currency: '',
            order_deadline: '',
            expected_arrival: '',
            confirmation_date: '',
            source_document: '',
            deliver_to: '',
            vendor_id: '',
            products: [{
                product_id: '',
                quantity: 0,
                unit_price: 0,
                taxes: 0,
                tax_excluded: 0,
                subtotal: 0
            }]
        });

        const productOptions = ref(['Product 1', 'Product 2', 'Product 3']);

        const totalTaxExcluded = computed(() => {
            return rfq.products.reduce((acc, product) => acc + product.tax_excluded, 0);
        });

        const totalTaxes = computed(() => {
            return rfq.products.reduce((acc, product) => acc + product.taxes, 0);
        });

        const total = computed(() => {
            return rfq.products.reduce((acc, product) => acc + product.subtotal, 0);
        });

        const showModal = ref(false);
        const showSuccessModal = ref(false);
        const modalAction = ref('');

        const openModal = (action) => {
            modalAction.value = action;
            showModal.value = true;
        };

        const confirmAction = () => {
            showModal.value = false;
            showSuccessModal.value = true;
        };

        const addProduct = () => {
            rfq.products.push({
                product_id: '',
                quantity: 0,
                unit_price: 0,
                taxes: 0,
                tax_excluded: 0,
                subtotal: 0
            });
        };

        const removeProduct = (index) => {
            rfq.products.splice(index, 1);
        };

        const updatePrice = (index) => {
            const product = rfq.products[index];
            product.tax_excluded = product.quantity * product.unit_price;
            product.subtotal = product.tax_excluded + product.taxes;
        };

        const submitForm = () => {
            console.log('Form submitted', rfq);
            showSuccessModal.value = true;
        };

        return {
            rfq,
            productOptions,
            totalTaxExcluded,
            totalTaxes,
            total,
            showModal,
            showSuccessModal,
            modalAction,
            openModal,
            confirmAction,
            addProduct,
            removeProduct,
            updatePrice,
            submitForm
        };
    }
};
</script>

<style>
    /* Add your custom styles here */
</style>
