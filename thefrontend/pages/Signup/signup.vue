<template>
    <div class="h-screen bg-slate-50 flex justify-center items-center w-full">
        <form @submit.prevent="submit">
            <div class="bg-white px-10 py-8 rounded-xl w-screen shadow-md max-w-sm">
                <img class="h-16 mb-6 mx-auto" src="/public/logoTrack.drawio.png" alt="">
                <div class="space-y-4">
                    <h1 class="text-center text-2xl font-semibold text-gray-600">Sign Up</h1>
                    <div>
                        <label for="name" class="block mb-1 text-gray-600 font-semibold">Name</label>
                        <input v-model="name" type="text"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
                    </div>
                    <div>
                        <label for="email" class="block mb-1 text-gray-600 font-semibold">Email</label>
                        <input v-model="email" type="text"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
                    </div>
                    <div>
                        <label for="jobTitle" class="block mb-1 text-gray-600 font-semibold">Job Title</label>
                        <select v-model="jobTitle" id="jobTitle"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full">
                            <option v-for="job in jobTitles" :key="job.id" :value="job.id">Manager</option>
                            <option v-for="job in jobTitles" :key="job.id" :value="job.id">Accounting Manager</option>
                            <option v-for="job in jobTitles" :key="job.id" :value="job.id">Purchase Manager</option>
                            <option v-for="job in jobTitles" :key="job.id" :value="job.id">Inventory Manager</option>
                        </select>
                    </div>
                    <div>
                        <label for="password" class="block mb-1 text-gray-600 font-semibold">Password</label>
                        <input v-model="password" type="password"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
                    </div>
                </div>
                <button class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md  tracking-wide">Signup</button>
                <div>
                    <p class="mt-5 text-sm font-light text-yellow-500 dark:text-black">
                        Already have an account? <nuxt-link to="/"
                            class="font-medium text-primary-600 hover:underline dark:text-yellow-500">Login
                        </nuxt-link>
                    </p>
                </div>
            </div>

        </form>
        <div>
            <!-- Render SuccessAlert Component -->
            <SuccessAlert v-if="alertMessage" :message="alertMessage" @close="alertMessage = ''" />
        </div>
    </div>

</template>

<script>
export default {
    name: "UserRegistration",
    data() {
        return {
            name: '',
            email: '',
            jobTitle: '',
            jobTitles: [],
            password: '',
            otp: '',
            showOtpInput: false,
            alertMessage: ''
        }
    },
    created() {
        this.fetchJobTitles();
    },
    methods: {
        async fetchJobTitles() {
            const response = await fetch('http://127.0.0.1:8000/jikoTrack/jobTitles'); 
            const data = await response.json();
            this.jobTitles = data;
        },
        async submit() {
            const response = await fetch('http://127.0.0.1:8000/jikoTrack/registerUser', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: this.name,
                    email: this.email,
                    password: this.password,
                    job_title: this.jobTitle
                })
            });

            const data = await response.json();
            if (response.ok) {
                if (data.message === 'Verify Your Account.OTP sent to your email') {
                    this.showOtpInput = true;
                }
                if (data.message === 'User Registered successfully.OTP sent to your email') {
                    this.showOtpInput = true;
                }

            } else {
                this.alertMessage = data.message || 'An error occurred';
            }
        },
        async verifyOtp() {
            const response = await fetch('http://127.0.0.1:8000/jikoTrack/verifyOTP', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: this.email,
                    otp: this.otp
                })
            });

            const data = await response.json();
            if (response.ok) {
                this.alertMessage = 'Account verified successfully';
                await this.$router.push('/home/manager');
            } else {
                this.alertMessage = data.message || 'An error occurred';
            }
        }
    }
}
</script>
