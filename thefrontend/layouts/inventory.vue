<template>
    <div>
        <header>
            <div class="dark:bg-gray-800 text-white">
                <div class="container mx-auto flex justify-between items-center p-4">
                    <div class="flex items-center">
                        <nuxt-link to="/inventory" class="flex items-center space-x-3 rtl:space-x-reverse">
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
                    <div class="relative">
                        <Profile />
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
        <div v-if="showPasswordInput" class="fixed inset-0 bg-black bg-opacity-50 z-50" @click="closeModal"></div>
        <div v-if="showPasswordInput" class="fixed inset-0 flex items-center justify-center z-50">
            <form @submit.prevent="verifyPassword" class="bg-white px-10 py-8 rounded-xl shadow-md max-w-sm w-full">
                <h1 class="text-center text-2xl font-semibold text-gray-600">Enter Password</h1>
                <div class="mt-4">
                    <label for="otp" class="block mb-1 text-gray-600 font-semibold">Password</label>
                    <input v-model="password" type="password"
                        class="bg-indigo-50 px-4 py-2 outline-none rounded-md w-full" />
                </div>
                <button class="mt-4 w-full bg-yellow-500 font-semibold py-2 rounded-md tracking-wide">Verify
                    Password</button>
            </form>
        </div>
    </div>
</template>

<script>

</script>
<style scoped>
.router-link-exact-active {
    color: rgb(251 191 36);
}
</style>