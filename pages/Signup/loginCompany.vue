<template>
    <div class="h-screen bg-slate-50 flex justify-center items-center w-full">
        <form @submit.prevent="submit">
            <div class="bg-white px-10 py-8 rounded-xl w-screen shadow-md max-w-sm">
                <img class="h-16 mb-6 mx-auto" src="/public/logoTrack.drawio.png" alt="">
                <div class="space-y-4">
                    <h1 class="text-center text-2xl font-semibold text-gray-600">Log In</h1>
                    <div>
                        <label for="email" class="block mb-1 text-gray-600 font-semibold">Email</label>
                        <input v-model="email" type="text"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
                    </div>
                    <div>
                        <label for="jobTitle" class="block mb-1 text-gray-600 font-semibold">Job Title</label>
                        <select v-model="jobTitle" id="jobTitle"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full">
                            <option v-for="job in jobTitles" :key="job.id" :value="job.id">{{ job.title }}</option>
                        </select>
                    </div>

                    <div>
                        <label for="password" class="block mb-1 text-gray-600 font-semibold">Password</label>
                        <input v-model="password" type="password"
                            class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
                    </div>
                </div>
                <button class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md  tracking-wide">Log In</button>
                <div>
                    <p class="mt-5 text-sm font-light text-yellow-500 dark:text-black">
                        Already have an account? <nuxt-link to="/Signup"
                            class="font-medium text-primary-600 hover:underline dark:text-yellow-500">Sign Up
                        </nuxt-link>
                    </p>
                </div>
            </div>

        </form>
        
        </div>
        <div>
            <!-- Render SuccessAlert Component -->
            <SuccessAlert v-if="alertMessage" :message="alertMessage" @close="alertMessage = ''" />
        </div>

</template>

<script>
// export default {
//     name: 'Login',
//     data() {
//         return {
//             email: '',
//             jobTitle: '',
//             jobTitles: [],
//             password: '',
//             alertMessage: '',
//             otp: ''
//         };
//     },
//     created() {
//         this.fetchJobTitles();
//     },
//     methods: {
//         async fetchJobTitles() {
//             const response = await fetch('http://127.0.0.1:8000/jikoTrack/jobTitles');
//             const data = await response.json();
//             this.jobTitles = data;
//         },
//         async submit() {
//             try {
//                 const response = await fetch('http://127.0.0.1:8000/jikoTrack/loginCompany', {
//                     method: 'POST',
//                     headers: { 'Content-Type': 'application/json' },
//                     credentials: 'include',
//                     body: JSON.stringify({
//                         email: this.email,
//                         password: this.password,
//                         jobTitle: this.jobTitle,
                        
//                     })
//                 });

//                 const data = await response.json();
//                 if (response.ok) {
//                     this.alertMessage = 'Login verified successfully';


//                     if (data.jwt) {

//                         localStorage.setItem('jwt', data.jwt);

//                         const selectedJobTitle = this.jobTitles.find(job => job.id === this.jobTitle);
//                         if (selectedJobTitle) {
//                             switch (selectedJobTitle.title) {
//                                 case 'Manager':
//                                     await this.$router.push('/home/manager');
//                                     break;
//                                 case 'Accounting Manager':
//                                     await this.$router.push('/accounting');
//                                     break;
//                                 case 'Purchase Manager':
//                                     await this.$router.push('/purchase');
//                                     break;
//                                 case 'Inventory Manager':
//                                     await this.$router.push('/inventory');
//                                     break;
//                             }
//                         } else {
//                             this.alertMessage = 'Invalid job title';
//                         }
//                     } else {
//                         this.alertMessage = 'Login failed (missing JWT token)';
//                     }
//                 } else {
//                     this.alertMessage = data.message || 'An error occurred';
//                 }
//             } catch (error) {
//                 this.alertMessage = 'An error occurred: ' + error.message;
//             }
//         }
//     }
// }
</script>