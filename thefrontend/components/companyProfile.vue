<template>
    <div class="bg-card text-card-foreground p-8 rounded-lg max-w-5xl mx-auto">
        <h2 class="text-3xl font-bold mb-6">Company Information</h2>
        <form id="companyForm" class="space-y-8" @submit.prevent="submitForm">
            <div class="flex items-center space-x-6">
                <div class="flex items-center justify-center w-full">
                    <label for="dropzone-file"
                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-white dark:hover:bg-white-100 dark:bg-white hover:bg-white-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                        <div class="flex flex-col items-center justify-center pt-5 pb-6">
                            <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                            </svg>
                            <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click
                                    to upload</span> or drag and drop</p>
                            <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)
                            </p>
                        </div>
                        <input id="dropzone-file" type="file" class="hidden" @change="previewLogo" />
                    </label>
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
                <div>
                    <label class="block text-sm font-medium mb-2" for="companyId">Company ID</label>
                    <input v-model="formData.companyId" type="text" id="companyId" name="companyId"
                        class="block w-full text-sm border border-input rounded-lg p-3 bg-background text-foreground"
                        placeholder="Company ID" />
                </div>
                <div>
                    <label class="block text-sm font-medium mb-2" for="address">Address</label>
                    <input v-model="formData.address" type="text" id="address" name="address"
                        class="block w-full text-sm border border-input rounded-lg p-3 bg-background text-foreground"
                        placeholder="Company Address" />
                </div>
                <div>
                    <label class="block text-sm font-medium mb-2" for="email">Email</label>
                    <input v-model="formData.email" type="email" id="email" name="email"
                        class="block w-full text-sm border border-input rounded-lg p-3 bg-background text-foreground"
                        placeholder="company@example.com" />
                </div>
                <div>
                    <label class="block text-sm font-medium mb-2" for="website">Website</label>
                    <input v-model="formData.website" type="text" id="website" name="website"
                        class="block w-full text-sm border border-input rounded-lg p-3 bg-background text-foreground"
                        placeholder="https://www.company.com" />
                </div>
                <div>
                    <label class="block text-sm font-medium mb-2" for="phone">Phone</label>
                    <input v-model="formData.phone" type="text" id="phone" name="phone"
                        class="block w-full text-sm border border-input rounded-lg p-3 bg-background text-foreground"
                        placeholder="Phone Number" />
                </div>
            </div>
            <button type="submit"
                class="bg-primary text-primary-foreground hover:bg-primary/80 p-3 rounded-lg mt-6">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            formData: {
                companyId: '',
                address: '',
                email: '',
                website: '',
                phone: ''
            },
            logoPreview: 'https://placehold.co/96x96'
        };
    },
    methods: {
        previewLogo(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = e => {
                    this.logoPreview = e.target.result;
                    this.uploadLogo(file);
                };
                reader.readAsDataURL(file);
            }
        },
        uploadLogo(file) {
            const formData = new FormData();
            formData.append('image', file);

            fetch('http://127.0.0.1:8000/backend/companies/logo/', {
                method: 'POST',
                body: formData,
                headers: {
                }
            })
                .then(response => response.json())
                .then(data => {
                    alert('logo updated successfully');
                    console.log('Success:', data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        submitForm() {
            fetch('http://127.0.0.1:8000/backend/companies/details/', {
                method: 'POST',
                body: JSON.stringify(this.formData),
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    }
};
definePageMeta({
    layout: 'home'
})
</script>

<style scoped>
/* Add scoped styles as needed */
</style>
