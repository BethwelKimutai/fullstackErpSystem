<template>
  <div class="text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700">
    <ul class="flex flex-wrap -mb-px justify-around">
      <li class="me-2" v-for="header in headers" :key="header">
        <a href="#"
          class="inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"
          aria-current="page">{{ header }}</a>
      </li>
    </ul>
  </div>
  <div>
    <div v-for="(product, index) in products" :key="index" class="flex items-center space-x-2 mb-2 bg-white text-black">
      <select v-model="product.id" @change="updateProduct(index)" class="flex-1 p-2 shadow bg-white text-black">
        <option v-for="option in productOptions" :value="option.id" :key="option.id">{{ option.name }}</option>
      </select>
      <input type="text" v-model="product.description" class="flex-1 p-2 shadow bg-white text-black" />
      <input type="number" v-model="product.quantity" @input="updateSubtotal(index)" class="flex-1 p-2 shadow bg-white text-black" />
      <input type="number" v-model="product.unitPrice" @input="updateSubtotal(index)" class="flex-1 p-2 shadow bg-white text-black" />
      <select v-model="product.unitOfMeasure" class="flex-1 p-2 shadow bg-white text-black">
        <option v-for="uom in unitOfMeasureOptions" :value="uom.id" :key="uom.id">{{ uom.name }}</option>
      </select>
      <input type="number" :value="product.subtotal" readonly class="w-24 p-2 shadow bg-white text-black" />
      <button @click="removeProduct(index)" class="p-2 shadow text-red-500 bg-white text-black">Remove</button>
    </div>
    <button @click="addProduct" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Add a product</button>
  </div>
  <div class="text-sm font-medium text-center text-gray-500 border-t border-gray-200 dark:text-gray-400 dark:border-gray-700 mt-4">
    <ul class="flex flex-wrap -mb-px justify-center">
      <li class="me-2">
        <a href="#"
          class="inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"
          aria-current="page">Grand Total: {{ grandTotal }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headers: ['Products', 'Description', 'Quantity', 'Unit Price', 'Unit Of Measure', 'Subtotal'],
      productOptions: [],
      unitOfMeasureOptions: [],
      products: [
        { id: '', description: '', quantity: 0, unitPrice: 0, unitOfMeasure: '', subtotal: 0 }
      ]
    }
  },
  computed: {
    grandTotal() {
      return this.products.reduce((sum, product) => sum + product.subtotal, 0);
    }
  },
  methods: {
    async fetchProductOptions() {
      // Fetch product options from your backend
      try {
        const response = await this.$axios.get('/api/products');
        this.productOptions = response.data;
      } catch (error) {
        console.error('Error fetching product options:', error);
      }
    },
    async fetchUnitOfMeasureOptions() {
      // Fetch unit of measure options from your backend
      try {
        const response = await this.$axios.get('/api/unit-of-measure');
        this.unitOfMeasureOptions = response.data;
      } catch (error) {
        console.error('Error fetching unit of measure options:', error);
      }
    },
    updateProduct(index) {
      // Update product details based on selected product id
      const selectedProduct = this.productOptions.find(p => p.id === this.products[index].id);
      if (selectedProduct) {
        this.products[index].description = selectedProduct.description;
        this.products[index].unitOfMeasure = selectedProduct.unitOfMeasure;
        this.updateSubtotal(index);
      }
    },
    updateSubtotal(index) {
      const product = this.products[index];
      product.subtotal = product.quantity * product.unitPrice;
    },
    addProduct() {
      this.products.push({ id: '', description: '', quantity: 0, unitPrice: 0, unitOfMeasure: '', subtotal: 0 });
    },
    removeProduct(index) {
      this.products.splice(index, 1);
    }
  },
  mounted() {
    this.fetchProductOptions();
    this.fetchUnitOfMeasureOptions();
  }
}
</script>

<style lang="scss" scoped>
/* Add your styles here */
</style>
