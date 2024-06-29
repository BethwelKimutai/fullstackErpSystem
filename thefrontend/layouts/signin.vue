<template>
    <div>
        <nav class="bg-white dark:bg-grey-800 border-b border-zinc-200 dark:bg-gray-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between h-16">
                    <div class="flex">
                        <div class="flex-shrink-0 flex items-center">
                            <img class="h-8 w-auto" src="https://placehold.co/100x40" alt="Logo" />
                        </div>
                        <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
                            <a href="#"
                                class="text-zinc-900 dark:text-white inline-flex items-center px-1 pt-1 text-sm font-medium">Apps</a>
                            <a href="#"
                                class="text-zinc-900 dark:text-white inline-flex items-center px-1 pt-1 text-sm font-medium">Community</a>
                            <a href="#"
                                class="text-zinc-900 dark:text-white inline-flex items-center px-1 pt-1 text-sm font-medium">Pricing</a>
                            <a href="#"
                                class="text-zinc-900 dark:text-white inline-flex items-center px-1 pt-1 text-sm font-medium">Contact</a>
                        </div>
                    </div>
                    <div class="hidden sm:ml-6 sm:flex sm:items-center">
                        <nuxt-link to="/Signup/login"
                            class="text-zinc-900 dark:text-white inline-flex items-center px-1 pt-1 text-sm font-medium">Sign
                            in</nuxt-link>
                        <nuxt-link to="/Signup/compApp" class="ml-4 bg-purple-600 text-white px-3 py-2 rounded-md text-sm font-medium">Try
                            it free</nuxt-link>
                    </div>
                </div>
            </div>
        </nav>
    </div>
    <div class="min-h-screen flex-1">
        <slot />
    </div>
    <div>
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

<script setup></script>


<style scoped>
.router-link-exact-active {
    color: rgb(251 191 36);
}
</style>