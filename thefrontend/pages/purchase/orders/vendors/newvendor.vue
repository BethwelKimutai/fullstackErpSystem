<template>
<<<<<<< HEAD
    <div class="flex min-h-screen items-start justify-start bg-white">
        <div class="w-full p-8">
            <div class="mx-auto max-w-7xl">
                <h1 class="text-4xl font-medium text-black">Create Vendor</h1>
                <p class="mt-3 text-black">Fill in the details below to create a new vendor:</p>

                <form @submit.prevent="submitForm" class="mt-10">
                    <div class="grid gap-6 sm:grid-cols-2">
                        <!-- Vendor Type -->
                        <div class="relative z-0 col-span-2">
                            <label class="text-gray-600">Vendor Type</label>
                            <div class="mt-2 flex">
                                <label class="mr-4 flex items-center text-gray-600">
                                    <input type="radio" name="type" value="individual" class="mr-2"
                                        v-model="formData.type" /> Individual
                                </label>
                                <label class="flex items-center text-gray-600">
                                    <input type="radio" name="type" value="company" class="mr-2"
                                        v-model="formData.type" /> Company
                                </label>
                            </div>
                        </div>

                        <!-- Individual Form -->
                        <div v-if="formData.type === 'individual'" class="relative z-0 col-span-2">
                            <input type="text" name="name" v-model="formData.name"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Your
                                Name</label>
                        </div>
                        <div v-if="formData.type === 'individual'" class="relative z-0 col-span-2">
                            <input type="text" name="company_name" v-model="formData.company_name"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Company
                                Name</label>
                        </div>

                        <!-- Company Form -->
                        <div v-if="formData.type === 'company'" class="relative z-0 col-span-2">
                            <input type="text" name="company_name" v-model="formData.company_name"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Company
                                Name</label>
                        </div>

                        <!-- Common Form Fields -->
                        <div class="relative z-0">
                            <input type="text" name="contact_street1" v-model="formData.contact_street1"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                                Primary Address</label>
                        </div>

                        <div class="relative z-0">
                            <input type="text" name="contact_street2" v-model="formData.contact_street2"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                                Secondary Address</label>
                        </div>

                        <div class="relative z-0">
                            <select name="contact_city" v-model="formData.contact_city"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0">
                                <option value="Nairobi">Nairobi</option>
                                <option value="Mombasa">Mombasa</option>
                                <option value="Kisumu">Kisumu</option>
                                <option value="Nakuru">Nakuru</option>
                            </select>
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">City</label>
                        </div>

                        <div class="relative z-0">
                            <select name="contact_state" v-model="formData.contact_state"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0">
                                <option value="Nairobi">Nairobi</option>
                                <option value="Coast">Coast</option>
                                <option value="Nyanza">Nyanza</option>
                                <option value="Rift Valley">Rift Valley</option>
                            </select>
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">State</label>
                        </div>

                        <div class="relative z-0">
                            <input type="text" name="contact_zip" v-model="formData.contact_zip"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">ZIP
                                Code</label>
                        </div>

                        <div class="relative z-0">
                            <select name="contact_country" v-model="formData.contact_country"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0">
                                <option value="Kenya">Kenya</option>
                            </select>
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Country</label>
                        </div>

                        <div class="relative z-0">
                            <input type="text" name="tax_id" v-model="formData.tax_id"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Tax
                                Identification Number</label>
                        </div>

                        <div v-if="formData.type === 'individual'" class="relative z-0">
                            <input type="text" name="phone" v-model="formData.mobile"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                                Phone Number</label>
                        </div>

                        <div v-if="formData.type === 'company'" class="relative z-0 ">
                            <input type="text" name="phone" v-model="formData.company_phone"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                                Phone Number</label>
                        </div>

                        <div class="relative z-0">
                            <input type="email" name="email" v-model="formData.email"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Email</label>
                        </div>
                        <div class="relative z-0">
                            <input type="url" name="website" v-model="formData.website"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Website</label>
                        </div>

                        <div class="relative z-0">
                            <input type="text" name="title" v-model="formData.title"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Title</label>
                        </div>

                        <div class="relative z-0">
                            <input type="text" name="tags" v-model="formData.tags"
                                class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" " />
                            <label
                                class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Tags</label>
                        </div>
                    </div>


                    <div class="mt-6 flex justify-end">
                        <button type="submit"
                            class="rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-500">Create
                            Vendor</button>
                    </div>
                </form>
            </div>
        </div>
=======
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
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356
    </div>
</template>

<script>
<<<<<<< HEAD
import {reactive, computed, onMounted } from 'vue';
import { useAuthStore } from '~/stores/auth';

const authStore = useAuthStore();

const formData = reactive({
    type: 'individual',
    name: '',
    company_name: '',
    contact_street1: '',
    contact_street2: '',
    contact_city: '',
    contact_state: '',
    contact_zip: '',
    contact_country: 'Kenya',
    tax_id: '',
    phone: '',
    mobile: '',
    email: '',
    vendor_company: '',
});

const vendorCompanyId = computed(() => {
    return authStore.auth_user ? authStore.auth_user.company_id : '';
});

onMounted(() => {
    formData.vendor_company = vendorCompanyId.value;
});

const submitForm = async () => {
    console.log('Submitted Form:', JSON.stringify(formData));

    try {
        const response = await fetch('http://127.0.0.1:8000/purchasebackend/vendors/createvendors/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Server Response:', data);
    } catch (error) {
        console.error('Error submitting form:', error);
    }
};

definePageMeta({
    layout: "purchase",
})

</script>
=======
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
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356
