<template>
  <div class="min-h-screen bg-slate-50 flex justify-center items-center">
    <form @submit.prevent="submit" class="w-full max-w-lg px-8">
      <div class="bg-white px-10 py-8 rounded-xl shadow-md w-full">
        <img class="h-16 mb-6 mx-auto" src="/public/logoTrack.drawio.png" alt="">
        <div class="space-y-4">
          <h1 class="text-center text-2xl font-semibold text-gray-600">Company Registration</h1>
          <div>
            <label for="companyName" class="block mb-1 text-gray-600 font-semibold">Company Name</label>
            <input v-model="companyName" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>
          <div>
            <label for="companyEmail" class="block mb-1 text-gray-600 font-semibold">Company Email</label>
            <input v-model="companyEmail" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label for="address" class="block mb-1 text-gray-600 font-semibold">Address</label>
              <input v-model="address" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
            </div>
            <div>
              <label for="country" class="block mb-1 text-gray-600 font-semibold">Country</label>
              <input v-model="country" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label for="city" class="block mb-1 text-gray-600 font-semibold">City</label>
              <input v-model="city" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
            </div>
            <div>
              <label for="zone" class="block mb-1 text-gray-600 font-semibold">Zone/Province</label>
              <input v-model="zone" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
            </div>
          </div>
          <div>
            <label for="contactNumber" class="block mb-1 text-gray-600 font-semibold">Contact Number</label>
            <input v-model="contactNumber" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>
          <div>
            <label for="password" class="block mb-1 text-gray-600 font-semibold">Password</label>
            <input v-model="password" type="password" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>
          <div>
            <label for="jobTitle" class="block mb-1 text-gray-600 font-semibold">Job Title</label>
            <select v-model="jobTitle" id="jobTitle" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full">
              <option v-for="job in jobTitles" :key="job.id" :value="job.id">{{ job.title }}</option>
            </select>
          </div>
        </div>
        <button class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md tracking-wide">Sign Up</button>
        <div>
          <p class="mt-5 text-sm font-light text-yellow-500 dark:text-black">
            Already have an account? <nuxt-link to="/"
              class="font-medium text-primary-600 hover:underline dark:text-yellow-500">Login</nuxt-link>
          </p>
        </div>
      </div>
    </form>
    <div>
      <div v-if="showOtpInput" class="fixed inset-0 bg-black bg-opacity-50 z-50" @click="closeModal"></div>
      <div v-if="showOtpInput" class="fixed inset-0 flex items-center justify-center z-50">
        <form @submit.prevent="verifyOtp" class="bg-white px-10 py-8 rounded-xl shadow-md max-w-sm w-full">
          <h1 class="text-center text-2xl font-semibold text-gray-600">Enter OTP</h1>
          <div class="mt-4">
            <label for="otp" class="block mb-1 text-gray-600 font-semibold">OTP</label>
            <input v-model="otp" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>
          <button @click="verifyOtp"
            class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md tracking-wide">Verify OTP</button>
        </form>
      </div>
    </div>
    <div>
      <!-- Render SuccessAlert Component -->
      <SuccessAlert v-if="alertMessage" :message="alertMessage" @close="alertMessage = ''" />
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanyRegistration",
  data() {
    return {
      companyName: '',
      companyEmail: '',
      address: '',
      country: '',
      city: '',
      zone: '',
      contactNumber: '',
      password: '',
      jobTitle: '',
      jobTitles: [],
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
      const response = await fetch('http://127.0.0.1:8000/jikoTrack/jobTitles'); // Add this line (ensure this endpoint exists and returns job titles)
      const data = await response.json();
      this.jobTitles = data;
    },
    async submit() {
      const response = await fetch('http://127.0.0.1:8000/jikoTrack/RegisterCompany', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: this.companyName,
          email: this.companyEmail,
          address: this.address,
          country: this.country,
          city: this.city,
          zone: this.zone,
          number: this.contactNumber,
          password: this.password,
          job_title: this.jobTitle
        })
      });

      const data = await response.json();
      if (response.ok) {
        if (data.message === 'Company registered successfully. OTP sent to your email') {
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
          email: this.companyEmail,
          otp: this.otp
        })
      });

      const data = await response.json();
      if (response.ok) {
        this.alertMessage = 'Account verified successfully';
        const selectedJobTitle = this.jobTitles.find(job => job.id === this.jobTitle);
        switch (selectedJobTitle.title) {
          case 'Manager':
            await this.$router.push('/home/manager');
            break;
          case 'Accounting Manager':
            await this.$router.push('/home/accounting-manager');
            break;
          case 'Purchase Manager':
            await this.$router.push('/home/purchase-manager');
            break;
          case 'Inventory Manager':
            await this.$router.push('/home/inventory-manager');
            break;
        }
      } else {
        this.alertMessage = data.message || 'An error occurred';
      }
    }
  }
}
</script>

<style scoped></style>