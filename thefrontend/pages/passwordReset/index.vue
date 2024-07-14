<template>
    <body class="font-mono bg-gray-400">
      <!-- Container -->
      <div class="container mx-auto">
        <div class="flex justify-center px-6 my-12">
          <!-- Row -->
          <div class="w-full xl:w-3/4 lg:w-11/12 flex">
            <!-- Col -->
            <div class="w-full h-auto bg-gray-400 hidden lg:block lg:w-1/2 bg-cover rounded-l-lg"
              style="background-image: url('https://source.unsplash.com/oWTW-jNGl9I/600x800')"></div>
            <!-- Col -->
            <div class="w-full lg:w-1/2 bg-white p-5 rounded-lg lg:rounded-l-none">
              <div class="px-8 mb-4 text-center">
                <h3 class="pt-4 mb-2 text-2xl">Forgot Your Password?</h3>
                <p class="mb-4 text-sm text-gray-700">
                  We get it, stuff happens. Just enter your username below and we'll send you a
                  link to reset your password!
                </p>
              </div>
              <form class="px-8 pt-6 pb-8 mb-4 bg-white rounded" @submit.prevent="resetPassword">
                <div class="mb-4">
                  <label class="block mb-2 text-sm font-bold text-gray-700" for="username">
                    Username
                  </label>
                  <input v-model="username" class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                    id="username" type="text" placeholder="Enter username..." />
                </div>
                <div class="mb-6 text-center">
                  <button class="w-full px-4 py-2 font-bold text-white bg-red-500 rounded-full hover:bg-red-700 focus:outline-none focus:shadow-outline" type="submit">
                    Reset Password
                  </button>
                </div>
                <hr class="mb-6 border-t" />
                <div class="text-center">
                  <nuxt-link to="/" class="inline-block text-sm text-blue-500 align-baseline hover:text-blue-800">
                    Already have an account? Login!
                  </nuxt-link>
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
                    <button class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md tracking-wide">
                      Verify OTP
                    </button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        otp: '',
        showOtpInput: false
      };
    },
    methods: {
      async resetPassword() {
        try {
          const response = await fetch('http://127.0.0.1:8000/backend/users/forgotpassword/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: this.username })
          });
  
          if (response.ok) {
            // Show OTP input modal
            this.showOtpInput = true;
          } else {
            const result = await response.json();
            alert(result.message || 'Error sending password reset email.');
          }
        } catch (error) {
          alert('An error occurred: ' + error.message);
        }
      },
      async verifyOtp() {
        try {
          const response = await fetch('http://127.0.0.1:8000/backend/users/forgotpasswordotpverification/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ otp: this.otp })
          });
  
          const result = await response.json();
  
          if (response.ok) {
            await this.$router.push('/passwordReset/newPassword');
            this.showOtpInput = false;
          } else {
            alert(result.message || 'Error verifying OTP.');
          }
        } catch (error) {
          alert('An error occurred: ' + error.message);
        }
      },
      closeModal() {
        this.showOtpInput = false;
      }
    }
  };
  </script>
  
  



  