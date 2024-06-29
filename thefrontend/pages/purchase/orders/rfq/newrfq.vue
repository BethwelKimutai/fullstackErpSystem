<template>
    <div class="p-4 max-w-4xl mx-auto bg-white shadow-md rounded-md">
        <!-- Buttons for actions -->
        <div class="mt-6 flex space-x-4">
            <button type="button" @click="createRFQ"
                class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Create RFQ
            </button>
            <button type="button" @click="sendRFQByEmail"
                class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Send By Email
            </button>
            <button type="button" @click="downloadRFQ"
                class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Download RFQ
            </button>
        </div>

        <!-- Form for RFQ details -->
        <div class="p-4 bg-card text-card-foreground">
            <form @submit.prevent="submitForm" class="space-y-4">
                <!-- Vendor, Currency, Order Deadline, Expected Arrival, Company, Deliver To, and Products -->
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label for="vendor" class="block text-sm font-medium text-muted-foreground">Vendor</label>
                        <select v-model="rfq.vendor" id="vendor"
                            class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary">
                            <option>Select Vendor</option>
                            <!-- Add options dynamically if needed -->
                        </select>
                    </div>
                    <div>
                        <label for="currency" class="block text-sm font-medium text-muted-foreground">Currency</label>
                        <input v-model="rfq.currency" type="text" id="currency"
                            class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary" />
                    </div>
                    <div>
                        <label for="order-deadline" class="block text-sm font-medium text-muted-foreground">Order
                            Deadline</label>
                        <input v-model="rfq.orderDeadline" type="date" id="order-deadline"
                            class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary" />
                    </div>
                    <div>
                        <label for="expected-arrival" class="block text-sm font-medium text-muted-foreground">Expected
                            Arrival</label>
                        <input v-model="rfq.expectedArrival" type="date" id="expected-arrival"
                            class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary" />
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label for="company" class="block text-sm font-medium text-muted-foreground">Company</label>
                        <select v-model="rfq.company" id="company"
                            class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary">
                            <option>Select Company</option>
                            <!-- Add options dynamically if needed -->
                        </select>
                    </div>
                    <div>
                        <label for="deliver-to" class="block text-sm font-medium text-muted-foreground">Deliver
                            To</label>
                        <input v-model="rfq.deliverTo" type="text" id="deliver-to"
                            class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary" />
                    </div>
                </div>
                
                <!-- Products list and total -->
                <div class="mt-6">
                    <h3 class="text-lg font-medium text-muted-foreground">Products</h3>
                    <div id="products-list" class="grid grid-cols-1 gap-4 mt-2 overflow-x-auto">
                        <div class="flex flex-wrap">
                            <div v-for="(product, index) in rfq.products" :key="index"
                                class="product-entry flex items-start space-x-4">
                                <div class="flex flex-col">
                                    <label for="product"
                                        class="block text-sm font-medium text-muted-foreground">Product</label>
                                    <select v-model="product.name"
                                        class="product-select mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary">
                                        <option>Select Product</option>
                                        <option v-for="option in productOptions" :key="option">{{ option }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col">
                                    <label for="quantity"
                                        class="block text-sm font-medium text-muted-foreground">Quantity</label>
                                    <input v-model="product.quantity" type="number"
                                        class="quantity-input mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                                        @input="updatePrice(index)" />
                                </div>
                                <div class="flex flex-col">
                                    <label for="price-per-unit"
                                        class="block text-sm font-medium text-muted-foreground">Price/Unit</label>
                                    <input v-model="product.pricePerUnit" type="number"
                                        class="price-per-unit-input mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                                        @input="updatePrice(index)" />
                                </div>
                                <div class="flex flex-col">
                                    <label for="price"
                                        class="block text-sm font-medium text-muted-foreground">Price</label>
                                    <input v-model="product.price" type="number"
                                        class="price-input mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                                        readonly />
                                </div>
                                <!-- Trash Bin Icon -->
                                <div class="flex items-center">
                                    <svg @click="removeProduct(index)" xmlns="http://www.w3.org/2000/svg"
                                        class="h-6 w-6 cursor-pointer text-red-500" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button type="button" @click="addProduct"
                        class="mt-2 px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">Add
                        Product</button>
                </div>
            </form>
        </div>
        <div class="mt-6">
            <label for="total" class="block text-sm font-medium text-muted-foreground">Total</label>
            <input v-model="totalPrice" type="number" id="total"
                class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                readonly />
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            rfq: {
                vendor: '',
                currency: '',
                orderDeadline: '',
                expectedArrival: '',
                company: '',
                deliverTo: '',
                products: []
            },
            productOptions: ['Product A', 'Product B', 'Product C'], // Example product options
            totalPrice: 0
        };
    },
    methods: {
        updatePrice(index) {
            const product = this.rfq.products[index];
            const quantity = parseFloat(product.quantity) || 0;
            const pricePerUnit = parseFloat(product.pricePerUnit) || 0;
            const price = quantity * pricePerUnit;
            this.$set(product, 'price', price.toFixed(2));
            this.calculateTotal();
        },
        calculateTotal() {
            let totalPrice = 0;
            this.rfq.products.forEach(product => {
                totalPrice += parseFloat(product.price) || 0;
            });
            this.totalPrice = totalPrice.toFixed(2);
        },
        addProduct() {
            this.rfq.products.push({
                name: '',
                quantity: 0,
                pricePerUnit: 0,
                price: 0
            });
        },
        submitForm() {
            // Handle form submission logic here
            console.log('RFQ submitted:', this.rfq);
            // Example: Reset form after submission
            this.rfq = {
                vendor: '',
                currency: '',
                orderDeadline: '',
                expectedArrival: '',
                company: '',
                deliverTo: '',
                products: []
            };
            this.totalPrice = 0;
        },
        removeProduct(index) {
            this.rfq.products.splice(index, 1);
            this.calculateTotal();
        },
        async createRFQ() {
            try {
                const response = await fetch('http://127.0.0.1:8000/purchasebackend/rfqs/create/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `JWT ${your_jwt_token}`
                    },
                    body: JSON.stringify(this.rfq)
                });
                if (response.ok) {
                    // Handle success
                    console.log('RFQ created successfully.');
                    // Reset form
                    this.rfq = {
                        vendor: '',
                        currency: '',
                        orderDeadline: '',
                        expectedArrival: '',
                        company: '',
                        deliverTo: '',
                        products: []
                    };
                    this.totalPrice = 0;
                } else {
                    // Handle error
                    console.error('Failed to create RFQ.');
                }
            } catch (error) {
                console.error('Error creating RFQ:', error);
            }
        },
        async sendRFQByEmail() {
            // Implement send by email functionality
        },
        async downloadRFQ() {
            // Implement download RFQ functionality
        }
    }
};
</script>

<style scoped>
/* Add your Tailwind CSS styles here */
</style>
