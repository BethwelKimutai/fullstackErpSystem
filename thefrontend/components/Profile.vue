<template>
  <div class="relative">
    <button id="avatarButton" class="flex items-center focus:outline-none ml-0.25">
      <img src="https://placehold.co/40x40" alt="Avatar" class="rounded-full">
    </button>
    <div id="dropdownMenu" class="hidden absolute right-0 mt-2 w-48 bg-white text-zinc-800 rounded-lg shadow-lg z-50">
      <div class="p-4">
        <p class="font-bold">{{ auth_user.username }}</p>
        <p class="text-sm text-zinc-600">{{ auth_user.email }}</p>
      </div>
      <div class="border-t border-zinc-200"></div>
      <nuxt-link to="/profiledemo" class="block px-4 py-2 hover:bg-zinc-100">My profile</nuxt-link>
      <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Account settings</nuxt-link>
      <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">My likes</nuxt-link>
      <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Collections</nuxt-link>
      <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Pro version</nuxt-link>
      <div class="border-t border-zinc-200"></div>
      <a href="#" class="block px-4 py-2 hover:bg-zinc-100" @click="logout">Logout</a>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth';

export default {
  setup() {
    const authStore = useAuthStore();
    const { auth_user } = storeToRefs(authStore);

    const logout = () => {
      authStore.logout();
    };

    onMounted(() => {
      const avatarButton = document.getElementById('avatarButton');
      const dropdownMenu = document.getElementById('dropdownMenu');

      if (avatarButton && dropdownMenu) {
        avatarButton.addEventListener('click', (event) => {
          event.stopPropagation();
          dropdownMenu.classList.toggle('hidden');
        });

        document.addEventListener('click', () => {
          dropdownMenu.classList.add('hidden');
        });
      } else {
        console.error('Elements not found');
      }
    });

    return {
      auth_user,
      logout,
    };
  },
};
</script>
