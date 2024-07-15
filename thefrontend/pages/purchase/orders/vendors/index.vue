<template>
  <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 pr-10 lg:px-8">
    <div
      class="align-middle rounded-tl-lg rounded-tr-lg inline-block w-full py-4 overflow-hidden bg-white shadow-lg px-12">
      <div class="flex justify-between mb-4">
        <div class="inline-flex border rounded w-7/12 px-2 lg:px-6 h-12 bg-transparent">
          <div class="flex flex-wrap items-stretch w-full h-full mb-6 relative">
            <div class="flex">
              <span
                class="flex items-center leading-normal bg-transparent rounded rounded-r-none border border-r-0 border-none lg:px-3 py-2 whitespace-no-wrap text-grey-dark text-sm">
                <svg width="18" height="18" class="w-4 lg:w-auto" viewBox="0 0 18 18" fill="none"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M8.11086 15.2217C12.0381 15.2217 15.2217 12.0381 15.2217 8.11086C15.2217 4.18364 12.0381 1 8.11086 1C4.18364 1 1 4.18364 1 8.11086C1 12.0381 4.18364 15.2217 8.11086 15.2217Z"
                    stroke="#455A64" stroke-linecap="round" stroke-linejoin="round" />
                  <path d="M16.9993 16.9993L13.1328 13.1328" stroke="#455A64" stroke-linecap="round"
                    stroke-linejoin="round" />
                </svg>
              </span>
            </div>
            <input type="text" v-model="searchQuery"
              class="flex-shrink flex-grow flex-auto leading-normal tracking-wide w-px flex-1 border border-none border-l-0 rounded rounded-l-none px-3 relative focus:outline-none text-xxs lg:text-xs lg:text-base text-gray-500 font-thin"
              placeholder="Search">
          </div>
        </div>
        <div class="w-60 flex justify-end space-x-2">
          <nuxt-link to="/purchase/orders/vendors/newvendor"
            class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">Register
            Vendor</nuxt-link>
        </div>
      </div>
    </div>
  </div>
  <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 pr-10 lg:px-8">
    <nuxt-link to="" v-for="user in filteredUsers" :key="user.id"
      class="block max-w-sm p-6 bg-black border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">

      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ user.type === 'individual' ?
        user.name : user.company_name }}</h5>
      <p class="font-normal text-gray-700 dark:text-gray-400">Email: {{ user.email }}</p>
      <p class="font-normal text-gray-700 dark:text-gray-400">Country: {{ user.contact_country }}</p>
    </nuxt-link>
  </div>


</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
const { auth_user } = storeToRefs(authStore);

const users = ref([])
const searchQuery = ref("")
const router = useRouter()

const fetchUsers = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/purchasebackend/vendors/getvendors/', {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({
        company_id: auth_user.value.company_id
      })
    })

    if (!response.ok) {
      throw new Error('Network response was not ok')
    }

    const data = await response.json()
    users.value = data
    window.dispatchEvent(new CustomEvent('auth', { detail: true }))
  } catch (e) {
    console.log(e);
    window.dispatchEvent(new CustomEvent('auth', { detail: false }))
  }
}

const filteredUsers = computed(() => {
  return users.value
    .filter(user => {
      const searchStr = searchQuery.value.toLowerCase()
      return (
        user.type.toLowerCase().includes(searchStr) ||
        user.name?.toLowerCase().includes(searchStr) ||
        user.company_name?.toLowerCase().includes(searchStr) ||
        user.email?.toLowerCase().includes(searchStr) ||
        user.contact_country?.toLowerCase().includes(searchStr)
      )
    })
    .map(user => ({
      id: user.id,
      type: user.type,
      name: user.type === 'individual' ? user.name : user.company_name,
      email: user.email,
      contact_country: user.contact_country || '-'
    }))
})

onMounted(fetchUsers)

definePageMeta({
  layout: "purchase",
})
</script>

<style scoped></style>
