<template>
    <div>
        <nav class="bg-gray-200 p-4">
            <div class="container mx-auto flex justify-between items-center">
                <div class="flex space-x-4 border-b-2 border-gray-300">
                    <nuxt-link to="/profiledemo" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
                        active-class="border-yellow-500">Profile</nuxt-link>
                    <nuxt-link to="/profiledemo/notifications"
                        class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
                        active-class="border-yellow-500">Notifications</nuxt-link>
                    <nuxt-link to="/profiledemo/password" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
                        active-class="border-yellow-500">Password</nuxt-link>
                    <nuxt-link to="/profiledemo/personalinfo"
                        class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
                        active-class="border-yellow-500">Personal Info</nuxt-link>
                </div>
            </div>
        </nav>
        <div class="min-h-screen flex-1">
            <slot />
        </div>
    </div>
</template>
<script>
definePageMeta({
    layout:'home'
})
</script>