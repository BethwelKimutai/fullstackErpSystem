<template>
    <div>
        <div class="py-16 bg-gray-50 overflow-hidden">
            <div class="container m-auto px-6 space-y-8 text-gray-500 md:px-12">
                <div>
                    <span class="text-gray-600 text-lg font-semibold"></span>
                    <h2 class="mt-4 text-2xl text-gray-900 font-bold md:text-4xl">Transfers
                        <br class="lg:block" hidden>
                    </h2>
                </div>
                <div
                    class="mt-16 grid border divide-x divide-y rounded-xl overflow-hidden sm:grid-cols-2 lg:divide-y-0 lg:grid-cols-3 xl:grid-cols-4">
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/invoice.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Receipts</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Receipts</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/cargo-truck.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Deliveries</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Deliveries</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>

                    <!-- <div class="relative group bg-gray-100 transition hover:z-[1] hover:shadow-2xl lg:hidden xl:block">
                        <div
                            class="relative p-8 space-y-8 border-dashed rounded-lg transition duration-300 group-hover:bg-white group-hover:border group-hover:scale-90">
                            <img src="https://tailus.io/sources/blocks/stacked/preview/images/avatars/metal.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    More features</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">Read more</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div> -->
                </div>
                <div>
                    <span class="text-gray-600 text-lg font-semibold"></span>
                    <h2 class="mt-4 text-2xl text-gray-900 font-bold md:text-4xl">Adjustments</h2>
                </div>

                <div
                    class="mt-16 grid border divide-x divide-y rounded-xl overflow-hidden sm:grid-cols-2 lg:divide-y-0 lg:grid-cols-3 xl:grid-cols-4">
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/stock.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Physical Inventory</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Physical Inventory</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/disposal.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Scrap</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">Scrap</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/landed-cost.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Landed Costs</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Landed Costs</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>

                </div>
                <div>
                    <span class="text-gray-600 text-lg font-semibold"></span>
                    <h2 class="mt-4 text-2xl text-gray-900 font-bold md:text-4xl">Procurement</h2>
                </div>

                <div
                    class="mt-16 grid border divide-x divide-y rounded-xl overflow-hidden sm:grid-cols-2 lg:divide-y-0 lg:grid-cols-3 xl:grid-cols-4">
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/restock.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Replenishment</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">Replenish stock</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
definePageMeta({
    layout: 'inventory',
})

</script>

<style></style>