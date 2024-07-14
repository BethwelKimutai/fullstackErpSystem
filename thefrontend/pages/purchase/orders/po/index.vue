<template>
  <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 pr-10 lg:px-8">
    <nav aria-label="breadcrumb" class="w-max">
          <ol class="flex flex-wrap items-center w-full bg-opacity-60 rounded-md bg-transparent p-0 transition-all">
              <li
                  class="flex items-center text-blue-gray-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-light-blue-500">
                  <nuxt-link to="/purchase">
                      <p
                          class="block antialiased font-sans text-sm leading-normal text-blue-900 font-normal opacity-50 transition-all hover:text-blue-500 hover:opacity-100">
                          dashboard</p>
                  </nuxt-link>
                  <span
                      class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
              </li>
              <li
                  class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                  <nuxt-link to="/purchase/orders/">
                      <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                          Orders</p>
                  </nuxt-link>
                  <span
                      class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>

              </li>
              <li
                  class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                  <nuxt-link to="/purchase/orders/po">
                      <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                          Purchase Orders</p>
                  </nuxt-link>

              </li>
          </ol>
      </nav>
    <!-- Search and action buttons section -->
    <div
      class="align-middle rounded-tl-lg rounded-tr-lg inline-block w-full py-4 overflow-hidden bg-white shadow-lg px-12">
      <div class="flex justify-between">
        <!-- Search input -->
        <div class="inline-flex border rounded w-7/12 px-2 lg:px-6 h-12 bg-white">
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
            <input type="text" v-model="searchVendor" @input="handleSearch"
              class="flex-shrink flex-grow flex-auto leading-normal tracking-wide w-px flex-1 border border-none border-l-0 rounded rounded-l-none px-3 relative focus:outline-none text-xxs lg:text-xs lg:text-base text-gray-500 font-thin bg-white"
              placeholder="Search Vendor" />
          </div>
        </div>
        <!-- Action buttons -->
        <div class="w-60 flex justify-end space-x-2">
          <nuxt-link to="/purchase/orders/po/newpo"
            class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
            New Purchase Order</nuxt-link>
        </div>
      </div>
    </div>

    <!-- Vendor list section -->
    <div
      class="align-middle inline-block min-w-full shadow overflow-hidden bg-white shadow-dashboard px-8 pt-3 rounded-bl-lg rounded-br-lg">
      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead>
            <tr>
              <th class="px-6 py-3 border-b-2 border-gray-300 text-left leading-4 text-blue-500 tracking-wider">ID</th>
              <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Vendor Name</th>
              <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Company</th>
              <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Email</th>
              <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Deadline</th>
              <th class="px-6 py-3 border-b-2 border-gray-300"></th>
            </tr>
          </thead>
          <tbody class="bg-white">
            <tr v-for="vendor in filteredVendors" :key="vendor.id">
              <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-500">
                <div class="flex items-center">
                  <div>
                    <div class="text-sm leading-5 text-gray-800">#{{ vendor.id }}</div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-500">
                <div class="text-sm leading-5 text-blue-900">{{ vendor.vendor_name }}</div>
              </td>
              <td class="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">{{
                vendor.contact_person }}</td>
              <td class="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">{{
                vendor.email }}</td>
              <td class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-500 text-sm leading-5">
                <button @click="viewDetails(vendor.id)"
                  class="px-5 py-2 mr-2 border-blue-500 border text-blue-500 rounded transition duration-300 hover:bg-blue-700 hover:text-white focus:outline-none">View
                  Details</button>
                <button @click="deleteVendor(vendor.id)"
                  class="px-5 py-2 bg-red-500 border text-white rounded transition duration-300 hover:bg-red-700 hover:text-white focus:outline-none">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const vendors = ref([]);
const searchVendor = ref('');

const fetchVendors = async () => {
try {
  const response = await fetch('http://127.0.0.1:8000/purchasebackend/pos/', {
    method: "GET",
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
  });

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  const data = await response.json();
  vendors.value = data;
} catch (error) {
  console.error('Failed to fetch vendors:', error);
}
};

const viewDetails = (vendorId) => {
router.push(`/home/vendorDetails/${vendorId}`);
};

const handleSearch = () => {
// Filter vendors based on search input
const searchTerm = searchVendor.value.toLowerCase();
filteredVendors.value = vendors.value.filter(vendor =>
  vendor.vendor_name.toLowerCase().includes(searchTerm)
);
};

const filteredVendors = ref([]);

onMounted(fetchVendors);

definePageMeta({
layout: 'purchase',
})
</script>

<style scoped>
/* Add your scoped styles here */
</style>
