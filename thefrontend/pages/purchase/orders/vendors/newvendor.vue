<template>
    <div class="p-4 max-w-4xl mx-auto bg-white shadow-md rounded-md">
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
                    <nuxt-link to="/purchase/orders/vendors">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            Vendors</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>

                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/vendors/newvendor">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            New Vendor</p>
                    </nuxt-link>

                </li>
            </ol>
        </nav>
    </div>
    <div class="p-4 max-w-4xl mx-auto bg-white shadow-md rounded-md">
        <header class="mb-4">
            <h1 class="text-2xl font-bold">Vendor Form</h1>
        </header>

        <form @submit.prevent="submitForm" class="space-y-4">
            <div class="flex items-center space-x-4">
                <label class="inline-flex items-center">
                    <input type="radio" value="individual" v-model="vendorType" class="form-radio" />
                    <span class="ml-2">Individual</span>
                </label>
                <label class="inline-flex items-center">
                    <input type="radio" value="company" v-model="vendorType" class="form-radio" />
                    <span class="ml-2">Company</span>
                </label>
            </div>

            <div v-if="vendorType === 'individual'" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium">Vendor Name</label>
                    <input type="text" v-model="formData.vendorName" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Company Name</label>
                    <input type="text" v-model="formData.companyName" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Contact</label>
                    <input type="text" v-model="formData.contactStreet1" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Country</label>
                    <input type="text" v-model="formData.contactCountry" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">City</label>
                    <input type="text" v-model="formData.city" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Tax ID</label>
                    <input type="text" v-model="formData.taxId" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Zip</label>
                    <input type="text" v-model="formData.zip" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Mobile</label>
                    <input type="text" v-model="formData.mobile" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Email</label>
                    <input type="email" v-model="formData.email" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
            </div>

            <div v-if="vendorType === 'company'" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium">Company Name</label>
                    <input type="text" v-model="formData.companyName" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Contact</label>
                    <input type="text" v-model="formData.contactStreet1" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Country</label>
                    <input type="text" v-model="formData.contactCountry" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">City</label>
                    <input type="text" v-model="formData.city" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">State</label>
                    <input type="text" v-model="formData.state" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Tax ID</label>
                    <input type="text" v-model="formData.taxId" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Zip</label>
                    <input type="text" v-model="formData.zip" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Phone</label>
                    <input type="text" v-model="formData.phone" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
                <div>
                    <label class="block text-sm font-medium">Website</label>
                    <input type="text" v-model="formData.website" required
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
                </div>
            </div>

            <div>
                <label class="block text-sm font-medium">Job Position</label>
                <input type="text" v-model="formData.jobPosition" required
                    class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer" />
            </div>

            <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md">Confirm</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            vendorType: 'individual',
            formData: {
                vendorName: '',
                companyName: '',
                contactStreet1: '',
                contactStreet2: '',
                contactCountry: '',
                city: '',
                state: '',
                taxId: '',
                zip: '',
                phone: '',
                mobile: '',
                website: '',
                email: '',
                jobPosition: '',
            },
        };
    },
    methods: {
        async submitForm() {
            try {
                const response = await axios.post('http://127.0.0.1:8000/purchasebackend/vendors/createvendors/', {
                    type: this.vendorType,
                    name: this.vendorType === 'individual' ? this.formData.vendorName : '',
                    company_name: this.formData.companyName,
                    contact_street1: this.formData.contactStreet1,
                    contact_street2: this.formData.contactStreet2,
                    contact_city: this.formData.city,
                    contact_state: this.vendorType === 'company' ? this.formData.state : '',
                    contact_zip: this.formData.zip,
                    contact_country: this.formData.contactCountry,
                    tax_id: this.formData.taxId,
                    job_position: this.formData.jobPosition,
                    phone: this.vendorType === 'company' ? this.formData.phone : '',
                    mobile: this.vendorType === 'individual' ? this.formData.mobile : '',
                    email: this.formData.email,
                    website: this.vendorType === 'company' ? this.formData.website : '',
                }, {
                    withCredentials: true,
                });

                if (response.data.status === 'success') {
                    alert('Form submitted successfully');
                } else {
                    alert('Failed to submit form');
                }
            } catch (error) {
                console.error('Error submitting form:', error);
                alert('An error occurred while submitting the form');
            }
        },
    },
};
definePageMeta({
    layout: 'purchase'
})
</script>

<style scoped>
/* Add your custom styles here */
</style>