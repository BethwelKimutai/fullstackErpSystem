<template>
    <div class="flex min-h-screen items-start justify-start bg-white">
        <div class="w-full p-8">
            <div class="mx-auto max-w-7xl">
                <h1 class="text-4xl font-medium text-black">New Purchase Order</h1>
                <p class="mt-3 text-black">Fill in the details below to create a new Purchase Order:</p>

                <form class="mt-10 grid grid-cols-2 gap-6">
                    <div class="relative z-0 col-span-2">
                        <input type="text" name="purchaseOrderReference"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                            placeholder=" " />
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                            Purchase Order Reference</label>
                    </div>
                    <div class="relative z-0">
                        <select name="companyName"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0">
                            <option value="companyName">Jenterprises</option>
                        </select>
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Company Name</label>
                    </div>
                    <div class="relative z-0">
                        <input type="date" name="orderDate"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                            placeholder=" " />
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                            Order Date</label>
                    </div>
                    <div class="relative z-0">
                        <input type="date" name="orderDeadline"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                            placeholder=" " />
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                            Order Deadline</label>
                    </div>
                    <div class="relative z-0">
                        <input type="date" name="expectedArrival"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                            placeholder=" " />
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                            Expected Arrival</label>
                    </div>
                    <div class="relative z-0">
                        <select name="currency"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0">
                            <option value="KSH">KSH</option>
                            <option value="USD">USD</option>
                            <option value="POUNDS">POUNDS</option>
                            <option value="YEN">YEN</option>
                        </select>
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Currency</label>
                    </div>
                    <div class="relative z-0">
                        <input type="text" name="PuchaseOrderNo"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                            placeholder=" " />
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">
                            Purchase Order Number</label>
                    </div>
                    <div class="relative z-0">
                        <select name="vendorCompany"
                            class="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0">
                            <option value="ven">Vendor</option>
                        </select>
                        <label
                            class="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600">Vendor Company</label>
                    </div>
                    
                    <!-- products -->
                    <div class="col-span-2 border border-gray-300 p-6 rounded-lg">
                        <Product />
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    // Add your script here
}
</script>

<style scoped>
/* Add your styles here */
</style>
