<template>
    <div class="relative">
      <button id="avatarButton" class="flex items-center focus:outline-none ml-0.25">
        <img src="https://placehold.co/40x40" alt="Avatar" class="rounded-full">
      </button>
      <div id="dropdownMenu" class="hidden absolute right-0 mt-2 w-48 bg-white text-zinc-800 rounded-lg shadow-lg z-50">
        <div class="p-4">
          <p class="font-bold">{{ username }}</p>
          <p class="text-sm text-zinc-600">{{ email }}</p>
        </div>
        <div class="border-t border-zinc-200"></div>
        <nuxt-link to="/profiledemo" class="block px-4 py-2 hover:bg-zinc-100">My profile</nuxt-link>
        <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Account settings</nuxt-link>
        <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">My likes</nuxt-link>
        <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Collections</nuxt-link>
        <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Pro version</nuxt-link>
        <div class="border-t border-zinc-200"></div>
        <a href="#" class="block px-4 py-2 hover:bg-zinc-100" @click="signOut">Sign out</a>
        <div class="border-t border-zinc-200"></div>
        <a href="#" class="block px-4 py-2 hover:bg-zinc-100" @click="logout">Logout</a>
      </div>
    </div>
  </template>
  
  <script>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router'; // Import useRouter to access the router instance
  
  export default {
    data() {
      return {
        companyName: '',
        username: '',
        email: '',
        dropdownVisible: false,
        auth: false,
        showPasswordInput: false, // Add state to show OTP input
        password: '',
      }
    },
    async mounted() {
      const router = useRouter(); // Get the router instance
      try {
        const response = await fetch('http://127.0.0.1:8000/backend/users/getuser/', {
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
        });
        if (response.ok) {
          const content = await response.json();
          this.companyName = content.company_name;
          this.username = content.username;
          this.email = content.email;
        } else {
          alert('You are not logged in');
          router.push('/Signup/login');
        }
      } catch (e) {
        alert('You are not logged in');
        router.push('/Signup/login');
      }
    },
    methods: {
      async logout() {
        try {
          const response = await fetch('http://127.0.0.1:8000/backend/users/logout/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            credentials: 'include', // Include cookies for logout to work
          });
  
          if (!response.ok) {
            throw new Error('Logout failed');
          }
  
          const data = await response.json();
          console.log(data.message); // Log success message for debugging
  
          // Clear user data and redirect to login
          this.companyName = '';
          this.username = '';
          this.email = '';
          this.auth = false;
  
          this.$router.push('/Signup/login');
        } catch (error) {
          console.error('Logout error:', error);
          alert('Logout failed. Please try again.');
        }
      },
      async signOut() {
        try {
          const response = await fetch('http://127.0.0.1:8000/backend/users/signout/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include'
          });
  
          if (response.ok) {
            this.showPasswordInput = true;
            const data = await response.json();
            console.log(data.message);
            alert('Signed out temporarily. Please enter your password to resume session.');
          } else {
            const errorData = await response.json();
            console.error(errorData.message);
            alert('Sign-out failed. Please try again.');
          }
        } catch (error) {
          console.error('Sign-out error:', error);
          alert('Sign-out failed. Please try again.');
        }
      },
      closeModal() {
        this.showPasswordInput = false;
      },
      async verifyPassword() {
        try {
          const response = await fetch('http://127.0.0.1:8000/backend/users/signin/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ password: this.password })
          });
  
          if (response.ok) {
            const data = await response.json();
            console.log(data.message); // Log success message for debugging
            this.showPasswordInput = false;
            alert('Sign-in successful and session resumed.');
          } else {
            const errorData = await response.json();
            console.error(errorData.message);
            alert('Sign-in failed. Please try again.');
          }
        } catch (error) {
          console.error('Sign-in error:', error);
          alert('Sign-in failed. Please try again.');
        }
      },
    },
    setup() {
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
    }
  }
  </script>
  