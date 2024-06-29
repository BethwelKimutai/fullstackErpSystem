<template>
  <div ref="modalContainer" @click.self="closeModal" class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75">
    <form @submit.prevent="submit" class="w-full max-w-lg px-8">
      <div class="bg-white px-10 py-8 rounded-xl w-screen shadow-md max-w-sm">
        <img class="h-14 mb-4 mx-auto" src="/public/logoTrack.drawio.png" alt="">
        <div class="space-y-4">
          <h1 class="text-center text-2xl font-semibold text-gray-600">Login</h1>
          <div>
            <label for="username" class="block mb-1 text-gray-600 font-semibold">Username</label>
            <input id="username" v-model="username" type="text"
              class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>

          <div>
            <label for="password" class="block mb-1 text-gray-600 font-semibold">Password</label>
            <input id="password" v-model="password" type="password"
              class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
          </div>
          <div class="flex items-center justify-between">
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="remember" aria-describedby="remember" type="checkbox"
                  class="w-4 h-4 border border-gray-300 rounded bg-yellow-500 focus:ring-3 focus:ring-yellow-500 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-yellow-500 dark:ring-offset-gray-800">
              </div>
              <div class="ml-3 text-sm">
                <label for="remember" class="text-gray-500 dark:text-black">Remember me</label>
              </div>
            </div>
            <nuxt-link to="/passwordReset"
              class="text-sm font-medium text-primary-600 hover:underline dark:text-yellow-500">Forgot
              password?</nuxt-link>
          </div>
        </div>
        <button @click="submit"
          class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md tracking-wide">Login</button>
        <div>
          <p class="mt-5 text-sm font-light text-yellow-500 dark:text-black">
            Don’t have an account yet? <nuxt-link to="/Signup/signup"
              class="font-medium text-primary-600 hover:underline dark:text-yellow-500">Sign
              up</nuxt-link>
          </p>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const alertMessage = ref('');
const router = useRouter();
const modalContainer = ref(null);

const submit = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/backend/users/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    });

    const data = await response.json();

    const userDetails = data.user_details;
    console.log(userDetails)

    if (userDetails.is_superuser) {
      alert('Login was successful.');
      router.push('/superuser');
    }else if (userDetails.is_manager) {
      alert('Login was successful.');
      router.push('/home/manager');
    }else if (userDetails.is_accounting_manager) {
      alert('Login was successful.');
      router.push('/accounting');
    } else if (userDetails.is_inventory_manager) {
      alert('Login was successful.');
      router.push('/inventory');
    } else if (userDetails.is_purchase_manager) {
      alert('Login was successful.');
      router.push('/purchase');
    } else {
      alertMessage.value = 'Invalid role';
    }
  
  } catch (error) {
    console.error("An error occurred:", error);
    alertMessage.value = 'An error occurred: ' + error.message;
  } 
}

const closeModal = () => {
  modalContainer.value.style.display = 'none';
}
</script>

<style scoped>
.bg-opacity-75 {
  background-color: rgba(0, 0, 0, 0.75);
}
</style>