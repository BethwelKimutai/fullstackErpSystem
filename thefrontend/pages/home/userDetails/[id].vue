<template>
  <div class="min-h-screen p-6 bg-gray-100 flex items-center justify-center">
    <div class="container max-w-screen-lg mx-auto">
      <div>
        <h2 class="font-semibold text-xl text-gray-600">User Details</h2>
        <p class="text-gray-500 mb-6">Manage user information</p>

        <div class="bg-white rounded shadow-lg p-4 px-4 md:p-8 mb-6">
          <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 lg:grid-cols-3">
            <div class="text-gray-600">
              <p class="font-medium text-lg">Edit User Details</p>
              <p>Please fill out the fields you want to change</p>
            </div>

            <div class="lg:col-span-2">
              <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-5">
                <div class="md:col-span-5">
                  <label for="username">Username</label>
                  <input type="text" v-model="user.username" id="username"
                    class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" />
                </div>

                <div class="md:col-span-5">
                  <label for="email">Email</label>
                  <input type="text" v-model="user.email" id="email" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50"
                    placeholder="email@domain.com" />
                </div>

                <div class="md:col-span-5">
                  <label for="role">Role</label>
                  <select v-model="user.role" id="role" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50">
                    <option value="Manager">Manager</option>
                    <option value="Admin">Admin</option>
                    <option value="User">User</option>
                    <option value="Accounting Manager">Accounting Manager</option>
                    <option value="Inventory Manager">Inventory Manager</option>
                    <option value="Purchase Manager">Purchase Manager</option>
                  </select>
                </div>

                <div class="md:col-span-5 text-right">
                  <div class="flex justify-between">
                    <button @click="updateUser"
                      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2">Update</button>
                    <button @click="cancel"
                      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ml-2">Cancel</button>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const user = ref({})
const router = useRouter()
const route = useRoute()

const fetchUser = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/backend/users/getuserbyid/${route.params.id}/`, {
      method: "GET",
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
    })

    if (!response.ok) {
      throw new Error('Network response was not ok')
    }

    const data = await response.json()
    user.value = data
  } catch (e) {
    console.error('Failed to fetch user', e)
  }
}

const updateUser = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/backend/users/updateuser/${route.params.id}/`, {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(user.value)
    })

    if (!response.ok) {
      throw new Error('Network response was not ok')
    }

    router.push('/home/users')
  } catch (e) {
    console.error('Failed to update user', e)
  }
}

const cancel = async () => {
  try {
    router.push('/home/users')
  } catch (e) {
    console.error('Failed to cancel', e)
  }
}

onMounted(fetchUser)
definePageMeta({   
  layout: "home",
})

</script>

<style scoped>
</style>
