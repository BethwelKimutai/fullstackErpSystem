<template>
    <div>
        <header>
            <div class="dark:bg-gray-800 text-white">
                <div class="container mx-auto flex justify-between items-center p-4">
                    <div class="flex items-center">
                        <nuxt-link to="/accounting" class="flex items-center space-x-3 rtl:space-x-reverse">
                            <img src="/public/logoTrack.drawio.png" class="h-8" alt="Logo" />
                            <span
                                class="self-center text-2xl font-semibold whitespace-nowrap text-yellow-500">JikoTrack</span>
                        </nuxt-link>
                    </div>
                    <nav class="flex space-x-4">
                        <ul
                            class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 dark:border-gray-700">
                            <li>
                                <nuxt-link to="/inventory"
                                    class="block py-2 pr-4 pl-3 text-white rounded bg-primary-700 lg:bg-transparent lg:text-primary-700 lg:p-0 dark:text-white">Overview</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/inventory/operations" class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700
                               ">Operations</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/inventory/products"
                                    class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700">Products</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/inventory/reporting"
                                    class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700">Reporting</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/inventory/Configurations"
                                    class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700">Configuration</nuxt-link>
                            </li>

                        </ul>
                    </nav>
                    <span class="text-sm mr-1">Company: {{ companyName || 'Loading...' }}</span>
                    <div class="relative">
                        <button id="avatarButton" class="flex items-center focus:outline-none ml-0.25">
                            <img src="https://placehold.co/40x40" alt="Avatar" class="rounded-full">
                        </button>
                        <div id="dropdownMenu"
                            class="hidden absolute right-0 mt-2 w-48 bg-white text-zinc-800 rounded-lg shadow-lg z-50">
                            <div class="p-4">
                                <p class="font-bold">{{ username }}</p>
                                <p class="text-sm text-zinc-600">{{ email }}</p>
                            </div>
                            <div class="border-t border-zinc-200"></div>
                            <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">My profile</nuxt-link>
                            <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Account settings</nuxt-link>
                            <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">My likes</nuxt-link>
                            <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Collections</nuxt-link>
                            <nuxt-link to="" class="block px-4 py-2 hover:bg-zinc-100">Pro version</nuxt-link>
                            <div class="border-t border-zinc-200"></div>
                            <a href="#" class="block px-4 py-2 hover:bg-zinc-100" @click="signout">Sign out</a>
                            <a href="#" class="block px-4 py-2 hover:bg-zinc-100" @click="logout">Logout</a>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="min-h-screen flex-1">
            <slot />
        </div>
        <footer class="bg-gray-50">
            <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 lg:px-8">
                <div class="sm:flex sm:items-center sm:justify-between">
                    <p class="mt-4 text-center text-sm text-gray-500 lg:mt-0 lg:text-center">
                        Copyright &copy; 2024. All rights reserved.
                    </p>
                </div>
            </div>
        </footer>
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
            dropdownVisible: false // Add a data property to track the dropdown visibility
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


<style scoped>
.router-link-exact-active {
    color: rgb(251 191 36);
}
</style>