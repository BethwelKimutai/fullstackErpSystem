<template>
    <div class="p-4 max-w-4xl mx-auto bg-white shadow-md rounded-md">
        <!-- Buttons for actions -->
        <div class="mt-6 flex space-x-4">
            <button type="submit" @click="createPO"
                    class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Create Purchase Order
            </button>
            <button type="button" @click="sendPOByEmail"
                    class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Send By Email
            </button>
            <button type="button" @click="downloadPO"
                    class="px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">
                Download Purchase Order
            </button>
        </div>

        <!-- Form for PO details -->
        <div class="p-4 bg-card text-card-foreground">
            <form @submit.prevent="submitForm" class="space-y-4">
                <!-- Vendor Reference, Currency, Order Deadline, Expected Arrival, Deliver To, and Products -->
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label for="vendor-reference"
                               class="block text-sm font-medium text-muted-foreground">Vendor Reference</label>
                        <input v-model="rfq.vendor_reference" type="text" id="vendor-reference"
                               class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                    </div>
                    <div>
                        <label for="currency"
                               class="block text-sm font-medium text-muted-foreground">Currency</label>
                        <input v-model="rfq.currency" type="text" id="currency"
                               class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                    </div>
                    <div>
                        <label for="order-deadline"
                               class="block text-sm font-medium text-muted-foreground">Order Deadline</label>
                        <input v-model="rfq.order_deadline" type="date" id="order-deadline"
                               class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                    </div>
                    <div>
                        <label for="expected-arrival"
                               class="block text-sm font-medium text-muted-foreground">Expected Arrival</label>
                        <input v-model="rfq.expected_arrival" type="date" id="expected-arrival"
                               class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                    </div>
                </div>
                <div>
                    <label for="deliver-to"
                           class="block text-sm font-medium text-muted-foreground">Deliver To</label>
                    <input v-model="rfq.deliver_to" type="text" id="deliver-to"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
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
                                            class="product-select mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary">
                                        <option>Select Product</option>
                                        <option v-for="(option, index) in productOptions" :key="index"
                                                :value="index + 1">{{ option }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col">
                                    <label for="quantity"
                                           class="block text-sm font-medium text-muted-foreground">Quantity</label>
                                    <input v-model="product.quantity" type="number"
                                           class="quantity-input mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                                           @input="updatePrice(index)"/>
                                </div>
                                <div class="flex flex-col">
                                    <label for="unit-price"
                                           class="block text-sm font-medium text-muted-foreground">Unit Price</label>
                                    <input v-model="product.unit_price" type="number"
                                           class="unit-price-input mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                                           @input="updatePrice(index)"/>
                                </div>
                                <div class="flex flex-col">
                                    <label for="subtotal"
                                           class="block text-sm font-medium text-muted-foreground">Subtotal</label>
                                    <input v-model="product.subtotal" type="number"
                                           class="subtotal-input mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                                           readonly/>
                                </div>
                                <!-- Trash Bin Icon -->
                                <div class="flex items-center">
                                    <svg @click="removeProduct(index)" xmlns="http://www.w3.org/2000/svg"
                                         class="h-6 w-6 cursor-pointer text-red-500" fill="none" viewBox="0 0 24 24"
                                         stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                              d="M6 18L18 6M6 6l12 12"/>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button type="button" @click="addProduct"
                            class="mt-2 px-4 py-2 bg-yellow-300 text-primary-foreground rounded-md shadow-sm hover:bg-yellow-500 hover:text-primary">Add
                        Product
                    </button>
                </div>
                <!-- Additional fields -->
                <div class="mt-6">
                    <label for="taxes"
                           class="block text-sm font-medium text-muted-foreground">Taxes</label>
                    <input v-model="rfq.taxes" type="number" id="taxes"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                </div>
                <div class="mt-6">
                    <label for="tax-excluded"
                           class="block text-sm font-medium text-muted-foreground">Tax Excluded</label>
                    <input v-model="rfq.tax_excluded" type="number" id="tax-excluded"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                </div>
                <div class="mt-6">
                    <label for="confirmation-date"
                           class="block text-sm font-medium text-muted-foreground">Confirmation Date</label>
                    <input v-model="rfq.confirmation_date" type="date" id="confirmation-date"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                </div>
                <div class="mt-6">
                    <label for="source-document"
                           class="block text-sm font-medium text-muted-foreground">Source Document</label>
                    <input v-model="rfq.source_document" type="text" id="source-document"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                </div>
                <div class="mt-6">
                    <label for="vendor-id"
                           class="block text-sm font-medium text-muted-foreground">Vendor ID</label>
                    <input v-model="rfq.vendor_id" type="text" id="vendor-id"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"/>
                </div>
                <!-- Total -->
                <div class="mt-6">
                    <label for="total" class="block text-sm font-medium text-muted-foreground">Total</label>
                    <input v-model="totalPrice" type="number" id="total"
                           class="mt-1 block w-full bg-input border border-border rounded-md shadow-sm focus:ring-primary focus:border-primary"
                           readonly/>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            rfq: {
                vendor_reference: '',
                currency: '',
                order_deadline: '',
                expected_arrival: '',
                deliver_to: '',
                taxes: 0,
                tax_excluded: 0,
                confirmation_date: '',
                source_document: '',
                vendor_id: '',
                products: []
            },
            productOptions: ['Product A', 'Product B', 'Product C'],
            totalPrice: 0
        };
    },
    methods: {
        // Method to create PO via API
        async createPO() {
            try {
                const response = await fetch('http://127.0.0.1:8000/purchasebackend/pos/create/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `JWT ${your_jwt_token}`
                    },
                    body: JSON.stringify(this.rfq)
                });
                if (response.ok) {
                    // Handle success
                    console.log('Purchase Order created successfully');
                    this.submitForm(); // Reset form after successful creation
                } else {
                    // Handle error
                    console.error('Failed to create Purchase Order');
                }
            } catch (error) {
                console.error('Error creating Purchase Order:', error);
            }
        },
        // Method to send PO by email via API
        async sendPOByEmail() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/purchasebackend/pos/${po_id}/email/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `JWT ${your_jwt_token}`
                    }
                });
                if (response.ok) {
                    // Handle success
                    console.log('Purchase Order sent by email successfully');
                } else {
                    // Handle error
                    console.error('Failed to send Purchase Order by email');
                }
            } catch (error) {
                console.error('Error sending Purchase Order by email:', error);
            }
        },
        // Method to download PO via API
        async downloadPO() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/purchasebackend/pos/${po_id}/print/`, {
                    method: 'GET',
                    headers: {
                        'Authorization': `JWT ${your_jwt_token}`
                    }
                });
                if (response.ok) {
                    // Convert response to blob and create a download link
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.style.display = 'none';
                    a.href = url;
                    a.download = `PO_${po_reference}.pdf`;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                } else {
                    // Handle error
                    console.error('Failed to download Purchase Order');
                }
            } catch (error) {
                console.error('Error downloading Purchase Order:', error);
            }
        },
        // Method to update price and subtotal
        updatePrice(index) {
            const product = this.rfq.products[index];
            product.subtotal = product.quantity * product.unit_price;
            this.calculateTotal();
        },
        // Method to calculate total price
        calculateTotal() {
            this.totalPrice = this.rfq.products.reduce((total, product) => total + product.subtotal, 0);
        },
        // Method to add a new product entry
        addProduct() {
            this.rfq.products.push({
                product_id: null,
                quantity: 0,
                unit_price: 0,
                subtotal: 0
            });
        },
        // Method to remove a product entry
        removeProduct(index) {
            this.rfq.products.splice(index, 1);
            this.calculateTotal();
        },
        // Method to submit form (you may need to define this based on your needs)
        submitForm() {
            // Logic to handle form submission (e.g., reset form state)
            this.rfq = {
                vendor_reference: '',
                currency: '',
                order_deadline: '',
                expected_arrival: '',
                deliver_to: '',
                taxes: 0,
                tax_excluded: 0,
                confirmation_date: '',
                source_document: '',
                vendor_id: '',
                products: []
            };
            this.totalPrice = 0;
        }
    }
};
</script>

<style scoped>
/* Add your Tailwind CSS styles here */
</style>
