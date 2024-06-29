<template>
    <div class="bg-white p-8 rounded-lg shadow-md mt-4 mx-auto max-w-4xl">
      <nav aria-label="breadcrumb" class="w-max">
            <ol class="flex flex-wrap items-center w-full bg-opacity-60 rounded-md bg-transparent p-0 transition-all">
                <li
                    class="flex items-center text-blue-gray-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-light-blue-500">
                    <nuxt-link to="/purchase">
                        <p
                            class="block antialiased font-sans text-sm leading-normal text-blue-900 font-normal opacity-50 transition-all hover:text-blue-500 hover:opacity-100">
                            dashboard</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>
                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            Orders</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>

                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/vendors">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            Vendors</p>
                    </nuxt-link>
                    <span
                        class="text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none">/</span>

                </li>
                <li
                    class="flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500">
                    <nuxt-link to="/purchase/orders/vendors/newvendor">
                        <p class="block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal">
                            New Vendor</p>
                    </nuxt-link>

                </li>
            </ol>
        </nav>
        
    </div>
</template>