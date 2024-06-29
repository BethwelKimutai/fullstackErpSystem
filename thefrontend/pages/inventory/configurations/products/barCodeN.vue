<template>
    <div>
      <div class="bg-white p-8 rounded-lg shadow-md mt-4 mx-auto max-w-4xl">
        <nav aria-label="breadcrumb" class="w-max">
          <ol class="flex flex-wrap items-center w-full bg-opacity-60 rounded-md bg-transparent p-0 transition-all">
            <li class="flex items-center text-blue-gray-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-light-blue-500">
              <nuxt-link to="/inventory">
                <p class="block antialiased font-sans text-sm leading-normal text-blue-900 font-normal opacity-50 transition-all hover:text-blue-500 hover:opacity-100">
                  dashboard
                </p>
              </nuxt-link>
              <span class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
            </li>
            <li class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
              <nuxt-link to="/inventory/configurations/">
                <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                  configuration
                </p>
              </nuxt-link>
              <span class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
            </li>
            <li class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
              <nuxt-link to="/inventory/configurations/barcode-nomenclatures">
                <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                  Barcode Nomenclatures
                </p>
              </nuxt-link>
            </li>
          </ol>
        </nav>
        <form @submit.prevent="submitForm">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium mb-1" for="name">Name</label>
              <input v-model="formData.name" type="text" id="name" name="name" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Name" />
            </div>
            <div>
              <label class="block text-sm font-medium mb-1" for="pattern">Pattern</label>
              <input v-model="formData.pattern" type="text" id="pattern" name="pattern" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Pattern" />
            </div>
            <div class="sm:col-span-2">
              <label class="block text-sm font-medium mb-1" for="description">Description</label>
              <textarea v-model="formData.description" id="description" name="description" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Description"></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium mb-1" for="company">Company</label>
              <input v-model="formData.company" type="text" id="company" name="company" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Company" />
            </div>
          </div>
          <button type="submit" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg">Submit</button>
        </form>
      </div>
      <div class="bg-white p-8 rounded-lg shadow-md mt-4 mx-auto max-w-4xl">
        <div class="align-middle inline-block min-w-full shadow overflow-hidden bg-white shadow-dashboard px-8 pt-3 rounded-bl-lg rounded-br-lg">
          <div class="overflow-x-auto">
            <table class="min-w-full">
              <thead>
                <tr>
                  <th class="px-6 py-3 border-b-2 border-gray-300 text-left leading-4 text-blue-500 tracking-wider">ID</th>
                  <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">Name</th>
                  <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">Pattern</th>
                  <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">Description</th>
                  <th class="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">Company</th>
                  <th class="px-6 py-3 border-b-2 border-gray-300"></th>
                </tr>
              </thead>
              <tbody class="bg-white">
                <tr v-for="barcode in barcodeNomenclatures" :key="barcode.id">
                  <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-500">
                    <div class="flex items-center">
                      <div>
                        <div class="text-sm leading-5 text-blue-900">{{ barcode.id }}</div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-500">
                    <div class="text-sm leading-5 text-blue-900">{{ barcode.name }}</div>
                  </td>
                  <td class="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">
                    {{ barcode.pattern }}
                  </td>
                  <td class="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">
                    {{ barcode.description }}
                  </td>
                  <td class="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">
                    {{ barcode.company }}
                  </td>
                  <td class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-500 text-sm leading-5">
                    <button @click="viewDetails(barcode)" class="px-5 py-2 mr-2 border-blue-500 border text-blue-500 rounded transition duration-300 hover:bg-blue-700 hover:text-white focus:outline-none">Update</button>
                    <button @click="deleteBarcodeNomenclature(barcode.id)" class="px-5 py-2 bg-red-500 border text-white rounded transition duration-300 hover:bg-red-700 hover:text-white focus:outline-none">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- Update Modal -->
      <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen"></span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div class="sm:flex sm:items-start">
                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <h3 class="text-lg leading-6 font-medium text-gray-900">Update Barcode Nomenclature</h3>
                  <div class="mt-2">
                    <form @submit.prevent="updateForm">
                      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                          <label class="block text-sm font-medium mb-1" for="update-name">Name</label>
                          <input v-model="selectedBarcode.name" type="text" id="update-name" name="name" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Name" />
                        </div>
                        <div>
                          <label class="block text-sm font-medium mb-1" for="update-pattern">Pattern</label>
                          <input v-model="selectedBarcode.pattern" type="text" id="update-pattern" name="pattern" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Pattern" />
                        </div>
                        <div class="sm:col-span-2">
                          <label class="block text-sm font-medium mb-1" for="update-description">Description</label>
                          <textarea v-model="selectedBarcode.description" id="update-description" name="description" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Description"></textarea>
                        </div>
                        <div>
                          <label class="block text-sm font-medium mb-1" for="update-company">Company</label>
                          <input v-model="selectedBarcode.company" type="text" id="update-company" name="company" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Company" />
                        </div>
                      </div>
                      <div class="mt-4">
                        <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-lg">Update</button>
                        <button type="button" @click="showModal = false" class="px-4 py-2 ml-2 bg-gray-500 text-white rounded-lg">Cancel</button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        formData: {
          name: '',
          pattern: '',
          description: '',
          company: ''
        },
        barcodeNomenclatures: [],
        selectedBarcode: null,
        showModal: false
      };
    },
    methods: {
      async fetchBarcodeNomenclatures() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/bcn/get/', {
            withCredentials: true
          });
          this.barcodeNomenclatures = response.data;
        } catch (error) {
          console.error('Error fetching barcode nomenclatures:', error.response.data);
        }
      },
      async submitForm() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/bcn/create/', this.formData, {
            withCredentials: true
          });
          console.log('Response:', response.data);
          this.fetchBarcodeNomenclatures();
        } catch (error) {
          console.error('Error:', error.response.data);
        }
      },
      viewDetails(barcode) {
        this.selectedBarcode = { ...barcode };
        this.showModal = true;
      },
      async updateForm() {
        try {
          const response = await axios.put(`http://127.0.0.1:8000/bcn/update/${this.selectedBarcode.id}/`, this.selectedBarcode, {
            withCredentials: true
          });
          console.log('Update Response:', response.data);
          this.showModal = false;
          this.fetchBarcodeNomenclatures();
        } catch (error) {
          console.error('Error updating barcode nomenclature:', error.response.data);
        }
      },
      async deleteBarcodeNomenclature(id) {
        try {
          await axios.delete(`http://127.0.0.1:8000/bcn/delete/${id}/`, {
            withCredentials: true
          });
          this.fetchBarcodeNomenclatures();
        } catch (error) {
          console.error('Error deleting barcode nomenclature:', error.response.data);
        }
      }
    },
    mounted() {
      this.fetchBarcodeNomenclatures();
    }
  };
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  </style>
  