<template>
  <div class="min-h-screen p-6 bg-gray-100 flex items-center justify-center">
    <div class="container max-w-screen-lg mx-auto">
      <div>
        <h2 class="font-semibold text-xl text-gray-600">New User</h2>
        <p class="text-gray-500 mb-6">Create a New User</p>

        <div class="bg-white rounded shadow-lg p-4 px-4 md:p-8 mb-6">
          <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 lg:grid-cols-3">
            <div class="text-gray-600">
              <p class="font-medium text-lg">Creating a new user</p>
              <p>Please fill out all the fields</p>
            </div>

            <div class="lg:col-span-2">
              <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-5">
                <div class="md:col-span-5">
                  <label for="username">Username</label>
                  <input type="text" v-model="user.username" id="username"
                    class="h-10 border mt-1 rounded px-4 w-full bg-gray-50"
                    placeholder="username" />
                </div>

                <div class="md:col-span-5">
                  <label for="email">Email</label>
                  <input type="text" v-model="user.email" id="email" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50"
                    placeholder="email@domain.com" />
                </div>

                <div class="md:col-span-5">
                  <label for="role">Role</label>
                  <select v-model="user.role" id="role" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50">
                    <option v-for="role in roles" :key="role.name" :value="role.name">{{ role.name }}</option>
                  </select>
                </div>

                <div class="md:col-span-5">
                  <label for="company">Company</label>
                  <select v-model="user.company" id="company" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50">
                    <option v-for="company in companies" :key="company.id" :value="company.id">{{ company.name }}</option>
                  </select>
                </div>

                <div class="md:col-span-5">
                  <label for="password">Password</label>
                  <input type="password" v-model="user.password" id="password" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50"
                    placeholder="********" />
                </div>

                <div class="md:col-span-5 text-right">
                  <div class="flex justify-between">
                    <button @click="createUser"
                      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2">Create</button>
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
import { useRouter } from 'vue-router'

const user = ref({ username: '', email: '', role: '', company: '', password: '' })
const roles = ref([])
const companies = ref([])
const router = useRouter()

const fetchRolesAndCompanies = async () => {
  try {
    const [rolesResponse, companiesResponse] = await Promise.all([
      fetch('http://127.0.0.1:8000/backend/users/roles/'),
      fetch('http://127.0.0.1:8000/backend/companies/getcompanies/')
    ])

    if (rolesResponse.ok) {
      roles.value = await rolesResponse.json()
    } else {
      console.error('Failed to fetch roles')
    }

    if (companiesResponse.ok) {
      companies.value = await companiesResponse.json()
    } else {
      console.error('Failed to fetch companies')
    }
  } catch (e) {
    console.error('Failed to fetch roles and companies', e)
  }
}

const createUser = async () => {
  try {
    console.log("User data before sending:", user.value)  // Debug log

    const response = await fetch('http://127.0.0.1:8000/backend/users/createuser/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(user.value)
    })

    if (!response.ok) {
      throw new Error('Network response was not ok')
    }

    const result = await response.json()
    console.log("API response:", result)  

    if (result.status === 'user created') {
      router.push('/superuser/viewUsers')
    }
  } catch (e) {
    console.error('Failed to create user', e)
  }
}

const cancel = () => {
  router.push('/superuser/viewUsers')
}

onMounted(fetchRolesAndCompanies)
</script>
