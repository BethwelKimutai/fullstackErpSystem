<template>
    <div>
        <div class="py-16 bg-gray-50 overflow-hidden">
            <div class="container mx-auto px-6 space-y-8 text-gray-500 md:px-12">
                <div>
                    <span class="text-gray-600 text-lg font-semibold">Main features</span>
                    <h2 class="mt-4 text-2xl text-gray-900 font-bold md:text-4xl">
                        A technology-first approach to payments <br class="lg:block" hidden> and finance
                    </h2>
                </div>
                <div class="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl rounded-lg">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/athome/accounting.png"
                                class="w-10" width="512" height="512" alt="burger illustration">
                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">Accounting</h5>
                                <p class="text-sm text-gray-600">Take a Look at how your business is doing financially</p>
                            </div>
                            <nuxt-link to="/Signup/login" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Your Accounts</span>
                                <span class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl rounded-lg">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/athome/purchase-order.png"
                                class="w-10" width="512" height="512" alt="trowel illustration">
                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">Purchase</h5>
                                <p class="text-sm text-gray-600">Make purchases, see Orders and Products</p>
                            </div>
                            <nuxt-link to="/Signup/login" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Purchases</span>
                                <span class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl rounded-lg">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/athome/inventory-management.png"
                                class="w-10" width="512" height="512" alt="package delivery illustration">
                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">Inventory</h5>
                                <p class="text-sm text-gray-600">Manage Your Inventory Here!</p>
                            </div>
                            <nuxt-link to="/Signup/login" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Inventory</span>
                                <span class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
definePageMeta({
    layout : "home"
})
</script>

<style>
.group-hover\:text-yellow-600:hover {
    color: #fbbf24;
}
</style>
