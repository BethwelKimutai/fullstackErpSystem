<template>
  <section class="bg-white dark:bg-gray-900">
    <nav class="container p-6 mx-auto lg:flex lg:justify-between lg:items-center">
      <div class="flex items-center justify-between">
        <a href="#">
          <img class="w-auto h-6 sm:h-7" src="/public/logoTrack.drawio.png" alt="">
        </a>
        <h1 class= "w-auto text-yellow-300 font-bold p-3 tracking-widest text-3xl">JIKOTRACK</h1>
        <!-- Mobile menu button -->
        <div class="flex lg:hidden">
          <button @click="toggleMenu" type="button" class="text-gray-500 dark:text-gray-200 hover:text-gray-600 dark:hover:text-gray-400 focus:outline-none focus:text-gray-600 dark:focus:text-gray-400" aria-label="toggle menu">
            <svg v-if="!isOpen" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 8h16M4 16h16" />
            </svg>
            <svg v-if="isOpen" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
      <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
      <div :class="{ 'block': isOpen, 'hidden': !isOpen }" class="absolute inset-x-0 z-20 w-full px-6 py-4 transition-all duration-300 ease-in-out bg-white shadow-md lg:bg-transparent lg:dark:bg-transparent lg:shadow-none dark:bg-gray-900 lg:mt-0 lg:p-0 lg:top-0 lg:relative lg:w-auto lg:flex lg:items-center">
        <div class="flex flex-col space-y-4 lg:mt-0 lg:flex-row lg:-px-8 lg:space-y-0">
          <a class="text-gray-700 transition-colors duration-300 transform lg:mx-8 dark:text-gray-200 dark:hover:text-blue-400 hover:text-blue-500" href="#">Home</a>
          <a class="text-gray-700 transition-colors duration-300 transform lg:mx-8 dark:text-gray-200 dark:hover:text-blue-400 hover:text-blue-500" href="#">Components</a>
          <a class="text-gray-700 transition-colors duration-300 transform lg:mx-8 dark:text-gray-200 dark:hover:text-blue-400 hover:text-blue-500" href="#">Pricing</a>
          <a class="text-gray-700 transition-colors duration-300 transform lg:mx-8 dark:text-gray-200 dark:hover:text-blue-400 hover:text-blue-500" href="#">Contact</a>
        </div>
        <a @click="showLoginPopup = true" class="block px-5 py-2 mt-4 text-sm text-center text-white capitalize bg-blue-600 rounded-lg lg:mt-0 hover:bg-blue-500 lg:w-auto" href="#">
          Get started
        </a>
      </div>
    </nav>

    <div class="container px-6 py-16 mx-auto text-center">
      <div class="max-w-lg mx-auto">
        <h1 class="text-3xl font-semibold text-gray-800 dark:text-white lg:text-4xl">Building Your Next App with our Awesome components</h1>
        <p class="mt-6 text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero similique obcaecati illum mollitia.</p>
        <nuxt-link to="/Signup/CompApp" class="px-5 py-2 mt-6 text-sm font-medium leading-5 text-center text-white capitalize bg-blue-600 rounded-lg hover:bg-blue-500 lg:mx-0 lg:w-auto focus:outline-none">
          Start 14-Day free trial
        </nuxt-link>
        <p class="mt-3 text-sm text-gray-400">No credit card required</p>
      </div>
      <div class="flex justify-center mt-10">
        <img class="object-cover w-full h-96 rounded-xl lg:w-4/5" src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80" />
      </div>
    </div>

    <!-- Login Modal -->
    <div v-if="showLoginPopup" ref="modalContainer" @click.self="closeLoginPopup" class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75">
      <form @submit.prevent="submitLogin" class="w-full max-w-lg px-8">
        <div class="bg-white px-10 py-8 rounded-xl w-screen shadow-md max-w-sm">
          <img class="h-14 mb-4 mx-auto" src="/public/logoTrack.drawio.png" alt="">
          <div class="space-y-4">
            <h1 class="text-center text-2xl font-semibold text-gray-600">Login</h1>
            <div>
              <label for="username" class="block mb-1 text-gray-600 font-semibold">Username</label>
              <input id="username" v-model="user.username" type="text" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full text-black" />
            </div>
            <div>
              <label for="password" class="block mb-1 text-gray-600 font-semibold">Password</label>
              <input id="password" v-model="user.password" type="password" class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full text-black" />
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-start">
                <div class="flex items-center h-5">
                  <input id="remember" aria-describedby="remember" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-yellow-500 focus:ring-3 focus:ring-yellow-500 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-yellow-500 dark:ring-offset-gray-800">
                </div>
                <div class="ml-3 text-sm">
                  <label for="remember" class="text-gray-500 dark:text-black">Remember me</label>
                </div>
              </div>
              <nuxt-link to="/passwordReset" class="text-sm font-medium text-primary-600 hover:underline dark:text-yellow-500">Forgot password?</nuxt-link>
            </div>
          </div>
          <button type="submit" class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md tracking-wide">Login</button>
          <div>
            <p class="mt-5 text-sm font-light text-yellow-500 dark:text-black">
              Don’t have an account yet? <nuxt-link to="/Signup/signup" class="font-medium text-primary-600 hover:underline dark:text-yellow-500">Sign up</nuxt-link>
            </p>
          </div>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const see_password = false;
import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth';


const {authenticateUser } = useAuthStore();
const { authenticated } = storeToRefs(useAuthStore());
const { profileUser } = useAuthStore();


const showLoginPopup = ref(false);
const isOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

const closeLoginPopup = () => {
  showLoginPopup.value = false;
};

const user = ref({
  username: "",
  password: "",
})

const submitLogin = async () => {
  try {
    await authenticateUser(user.value);
    console.log("this is the auth", authenticated)
    if(authenticated.value){
      await profileUser();
    }
  } catch (error) {
    console.error('Login failed:', error);
  }
};
</script>

<style scoped>
.bg-opacity-75 {
  background-color: rgba(0, 0, 0, 0.75);
}
</style>

