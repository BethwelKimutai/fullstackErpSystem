<template>
    <div>
        <div class="py-16 bg-gray-50 overflow-hidden">
            <div class="container m-auto px-6 space-y-8 text-gray-500 md:px-12">
                <div>
                    <span class="text-gray-600 text-lg font-semibold"></span>
                    <h2 class="mt-4 text-2xl text-gray-900 font-bold md:text-4xl">Customers<br class="lg:block" hidden></h2>
                </div>
                <div
                    class="mt-16 grid border divide-x divide-y rounded-xl overflow-hidden sm:grid-cols-2 lg:divide-y-0 lg:grid-cols-3 xl:grid-cols-4">
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/accounting/invoices.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Invoices</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/invoices" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Invoices</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/accounting/payment-method.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Credit Notes</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/creditNotes" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See my Credits Notes</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
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
                            <nuxt-link to="/accounting/customers/receipts" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Receipts</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/accounting/file.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Amounts to Settle</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/amountsToSettle" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">Amounts to Settle</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    
                </div>
                <!-- Second customers row -->
                <div
                    class="mt-16 grid border divide-x divide-y rounded-xl overflow-hidden sm:grid-cols-2 lg:divide-y-0 lg:grid-cols-3 xl:grid-cols-4">
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/accounting/payment-method.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Payments</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/payments" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Payments</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/accounting/follow-up.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Follow-up reports</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/followUpReports" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Follow up reports</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/online-shopping.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Products</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/products" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See products</span>
                                <span
                                    class="-translate-x-4 opacity-0 text-2xl transition duration-300 group-hover:opacity-100 group-hover:translate-x-0">&RightArrow;</span>
                            </nuxt-link>
                        </div>
                    </div>
                    <div class="relative group bg-white transition hover:z-[1] hover:shadow-2xl">
                        <div class="relative p-8 space-y-8">
                            <img src="/public/accounting/public-service.png"
                                class="w-10" width="512" height="512" alt="burger illustration">

                            <div class="space-y-2">
                                <h5 class="text-xl text-gray-800 font-medium transition group-hover:text-yellow-600">
                                    Customers</h5>
                                <p class="text-sm text-gray-600">Neque Dolor, fugiat non cum doloribus aperiam
                                    voluptates nostrum.</p>
                            </div>
                            <nuxt-link to="/accounting/customers/customers" class="flex justify-between items-center group-hover:text-yellow-600">
                                <span class="text-sm">See Customers</span>
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
    layout: 'accounting',
})

</script>

<style></style>