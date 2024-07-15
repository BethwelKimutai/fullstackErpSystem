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
                    <nuxt-link to="/profiledemo/compProfile"
                        class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
                        active-class="border-yellow-500">Company Info</nuxt-link>
                </div>
                <div class="flex flex-col-reverse justify-between gap-6 md:flex-row md:items-center">
                    <div class="flex items-center">
                        <Profile />
                    </div>
                </div>
            </div>
        </nav>
        <div class="bg-white p-8 rounded-lg shadow-md mt-4 mx-auto max-w-4xl">
            <div class="p-6 max-w-xl mx-auto">
                <div class="mb-4">
                    <h2 class="text-xl font-bold">Password <span class="text-zinc-400 text-sm">(i)</span></h2>
                </div>
                <div class="space-y-4">
                    <div class="flex items-center">
                        <label class="w-1/3 text-zinc-700">Current password</label>
                        <div class="w-2/3 relative">
                            <input type="password" placeholder="Enter current password"
                                class="w-full p-2 border rounded-lg" />
                            <img aria-hidden="true" alt="eye" src="https://placehold.co/20x20"
                                class="absolute right-2 top-2" />
                        </div>
                    </div>
                    <div class="flex items-center">
                        <label class="w-1/3 text-zinc-700">New password</label>
                        <div class="w-2/3 relative">
                            <input type="password" placeholder="Enter new password"
                                class="w-full p-2 border rounded-lg" />
                            <img aria-hidden="true" alt="eye" src="https://placehold.co/20x20"
                                class="absolute right-2 top-2" />
                        </div>
                    </div>
                    <div class="flex items-center">
                        <label class="w-1/3 text-zinc-700">Repeat new password</label>
                        <div class="w-2/3 relative">
                            <input type="password" placeholder="Repeat new password"
                                class="w-full p-2 border rounded-lg" />
                            <img aria-hidden="true" alt="eye" src="https://placehold.co/20x20"
                                class="absolute right-2 top-2" />
                        </div>
                    </div>
                    <div class="flex items-center">
                        <label class="w-1/3 text-zinc-700">Level:</label>
                        <div class="w-2/3 flex space-x-2">
                            <div class="h-2 w-1/5 bg-blue-200 rounded"></div>
                            <div class="h-2 w-1/5 bg-blue-200 rounded"></div>
                            <div class="h-2 w-1/5 bg-blue-200 rounded"></div>
                            <div class="h-2 w-1/5 bg-blue-200 rounded"></div>
                            <div class="h-2 w-1/5 bg-blue-200 rounded"></div>
                        </div>
                    </div>
                    <div class="flex items-center">
                        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg">Change</button>
                        <a href="#" class="ml-4 text-blue-500">I forgot my password</a>
                    </div>
                </div>
            </div>
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