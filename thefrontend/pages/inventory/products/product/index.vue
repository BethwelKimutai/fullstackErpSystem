<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
    <div v-for="product in products" :key="product.id" class="border rounded-lg p-4 flex justify-between items-center dark:bg-zinc-800">
      <div class="flex items-center">
        <img :src="product.image" alt="Product Image" class="mr-4">
        <div>
          <h2 class="font-semibold text-black dark:text-white">{{ product.name }}</h2>
          <p class="text-zinc-500 dark:text-zinc-400">{{ product.code }}</p>
          <p>Price: $ {{ product.price }}</p>
          <p>On hand: {{ product.on_hand }} Units</p>
        </div>
      </div>
      <button @click="editProduct(product)" class="text-zinc-500 dark:text-zinc-400">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: []
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:8000//inventorybackend/getproduct')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    editProduct(product) {
      // Implement edit functionality, perhaps using a modal or form
      console.log('Editing product:', product);
      // Example: Redirect to edit page or open modal
      // this.$router.push({ name: 'EditProduct', params: { id: product.id } });
    }
  }
};
</script>

<style scoped>
/* Add your scoped styles here */
</style>