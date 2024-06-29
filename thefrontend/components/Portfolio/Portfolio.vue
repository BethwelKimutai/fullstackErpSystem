<template>
    <section class="bg-white dark:bg-gray-900">
      <div class="container px-6 py-12 mx-auto">
        <h1 class="text-2xl font-semibold text-gray-800 lg:text-3xl dark:text-white">Portfolio</h1>
  
        <div class="mt-8 xl:mt-16 lg:flex lg:-mx-12">
          <div class="lg:mx-12">
            <h1 class="text-xl font-semibold text-gray-800 dark:text-white">Table of Content</h1>
  
            <div class="mt-4 space-y-4 lg:mt-8">
              <a @click.prevent="selectedSection = 'webDesign'" href="#" class="block text-blue-500 dark:text-blue-400 hover:underline">Web design</a>
              <a @click.prevent="selectedSection = 'appDesign'" href="#" class="block text-gray-500 dark:text-gray-300 hover:underline">App design</a>
              <a @click.prevent="selectedSection = 'branding'" href="#" class="block text-gray-500 dark:text-gray-300 hover:underline">Branding</a>
              <a @click.prevent="selectedSection = 'animation'" href="#" class="block text-gray-500 dark:text-gray-300 hover:underline">Animation</a>
            </div>
          </div>
  
          <div class="flex-1 mt-8 lg:mx-12 lg:mt-0">
            <component :is="selectedSection"></component>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import WebDesign from './WebDesign.vue';
  import AppDesign from './AppDesign.vue';
  import Branding from './Branding.vue';
  import Animation from './Animation.vue';
  
  export default {
    components: {
      webDesign: WebDesign,
      appDesign: AppDesign,
      branding: Branding,
      animation: Animation,
    },
    data() {
      return {
        selectedSection: 'webDesign',
      };
    },
  };
  </script>
  
  <style scoped>
  /* Add any styles specific to the Portfolio component here */
  </style>
  