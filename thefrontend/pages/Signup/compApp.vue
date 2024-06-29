<template>
    <div>

        <body class="bg-white dark:bg-white p-6">
            <div id="app" class="flex flex-col lg:flex-row">
                <div class="bg-white dark:bg-white p-8 rounded-lg shadow-md w-full lg:w-2/3">
                    <h1 class="text-2xl font-bold text-teal-600 dark:text-teal-400">JikoTrack | Get Started</h1>
                    <p class="mt-2 text-zinc-600 dark:text-zinc-300">Apply now!.</p>
                    <form @submit.prevent="submitForm" class="mt-6 space-y-4">
                        <div>
                            <label class="block text-zinc-700 dark:text-zinc-400">Full Name</label>
                            <input v-model="form.name" type="text" name="name"
                                class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                        </div>
                        <div>
                            <label class="block text-zinc-700 dark:text-zinc-400">Email</label>
                            <input v-model="form.email" type="email" name="email"
                                class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                        </div>
                        <div>
                            <label class="block text-zinc-700 dark:text-zinc-400">Password</label>
                            <input v-model="form.password" type="password" name="password"
                                class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                        </div>
                        <div>
                            <label class="block text-zinc-700 dark:text-zinc-400">Company Name</label>
                            <input v-model="form.companyName" type="text" name="companyName"
                                class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                        </div>
                        <div class="flex space-x-4">
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Country</label>
                                <select v-model="form.country" name="country"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                                    <option>Kenya</option>
                                    <option>Rwanda</option>
                                    <option>Uganda</option>
                                    <option>Tanzania</option>
                                </select>
                            </div>
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Phone Number</label>
                                <input v-model="form.number" type="text" name="number" class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">

                            </div>
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Address</label>
                                <input v-model="form.address" type="text" name="address"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                            </div>
                        </div>
                        <div class="flex space-x-4">
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Language</label>
                                <select v-model="form.language" name="language"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                                    <option>English</option>
                                </select>
                            </div>
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Primary Interest</label>
                                <select v-model="form.primaryInterest" name="primaryInterest"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                                    <option>Use it in my Company</option>
                                    <option>Offer JikoTrack services to other Companies</option>
                                    <option>I am a Student</option>
                                </select>
                            </div>
                        </div>
                        <div class="flex space-x-4">
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Company Size</label>
                                <select v-model="form.companySize" name="companySize"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                                    <option>less than 5 employees</option>
                                    <option>5-20 employees</option>
                                    <option>20-50 employees</option>
                                    <option>50-250 employees</option>
                                    <option>>250 employees</option>
                                </select>
                            </div>
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">City</label>
                                <select v-model="form.city" name="city"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                                    <option>Nairobi</option>
                                    <option>Mombasa</option>
                                    <option>Kisumu</option>
                                    <option>Eldoret</option>
                                </select>
                            </div>
                            <div class="w-1/2">
                                <label class="block text-zinc-700 dark:text-zinc-400">Zone/Province</label>
                                <input v-model="form.zone" type="text" name="address"
                                    class="w-full mt-1 p-2 border border-zinc-300 dark:border-zinc-600 rounded-md focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-indigo-50">
                            </div>
                        </div>
                        <p class="text-zinc-600 dark:text-zinc-400 text-sm mt-4">By clicking on <strong>Start
                                Now</strong>, you accept our <a href="#"
                                class="text-teal-600 dark:text-teal-400">Subscription Agreement</a> and <a href="#"
                                class="text-teal-600 dark:text-teal-400">Privacy Policy</a>.</p>
                        <div class="flex space-x-4 mt-6">
                            <button type="button"
                                class="flex-1 bg-white border border-teal-600 dark:border-teal-400 text-teal-600 dark:text-teal-400 p-2 rounded-md hover:bg-zinc-50 dark:hover:bg-zinc-600">Change
                                apps selection</button>
                            <button type="submit"
                                class="flex-1 bg-teal-600 dark:bg-teal-400 text-white p-2 rounded-md hover:bg-teal-700 dark:hover:bg-teal-500">Start
                                Now</button>
                        </div>
                    </form>
                </div>
                <div class="mt-8 lg:mt-0 lg:ml-8 w-full lg:w-1/3">
                    <div class="bg-indigo-500 dark:bg-indigo-500 p-6 rounded-lg shadow-md">
                        <div class="flex items-center space-x-4">
                            <img src="https://placehold.co/40x40" alt="SAP Logo" class="w-10 h-10 rounded-full">
                            <div>
                                <h2 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">SAP Digital Supply Chain
                                </h2>
                                <p class="text-sm text-zinc-600 dark:text-zinc-400">@SCMatSAP</p>
                            </div>
                        </div>
                        <p class="mt-4 text-zinc-700 dark:text-zinc-300">Have you found the secret of supply chain
                            efficiency in disruption? Read the Oxford Economics Study to see what we learned</p>
                    </div>
                    <div class="bg-indigo-500 dark:bg-indigo-500 p-6 rounded-lg shadow-md mt-6">
                        <div class="flex items-center space-x-4">
                            <img src="https://placehold.co/40x40" alt="User Avatar" class="w-10 h-10 rounded-full">
                            <div>
                                <h2 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">Dr. Dilkhush</h2>
                                <p class="text-sm text-zinc-600 dark:text-zinc-400">@DrDilkhush</p>
                            </div>
                        </div>
                        <p class="mt-4 text-zinc-700 dark:text-zinc-300">Yup- our company finally figured it out. The
                            secret is to reduce expense on SAP, reduce complexity and cost, and switch to a 21st century
                            customer-centric solution like @JikoTrack. The whole implementation cost us less than AMC of
                            our bloated SAP system. Best move we made. Bye, SAP!</p>
                    </div>
                </div>
            </div>
        </body>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                name: '',
                email: '',
                password: '',
                companyName: '',
                country: '',
                number: '+254',
                address: '',
                language: '',
                primaryInterest: '',
                companySize: '',
                city: '',
                zone:''
            }
        }
    },
    methods: {
        async submitForm() {
            try {
                const response = await fetch('http://127.0.0.1:8000/backend/companies/register/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    },
                    body: JSON.stringify({
                        name: this.form.name, // Use this.form.name instead of this.name
                        email: this.form.email,
                        password: this.form.password,
                        companyName: this.form.companyName,
                        country: this.form.country,
                        number: this.form.number,
                        address: this.form.address,
                        language: this.form.language,
                        primaryInterest: this.form.primaryInterest,
                        companySize: this.form.companySize,
                        city: this.form.city,
                        zone: this.form.zone,
                    })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    alert('Error: ' + JSON.stringify(errorData));
                } else {
                    const responseData = await response.json();
                    alert('Registration successful. Status: ' + responseData.status);
                    this.$router.push('/');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        }
    }
}
</script>
