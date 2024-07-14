<template>
  <div>
    <nav class="bg-gray-200 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <div class="flex space-x-4 border-b-2 border-gray-300">
          <nuxt-link to="/profiledemo" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
            active-class="border-yellow-500">Profile</nuxt-link>
          <nuxt-link to="/profiledemo/notifications" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
            active-class="border-yellow-500">Notifications</nuxt-link>
          <nuxt-link to="/profiledemo/password" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
            active-class="border-yellow-500">Password</nuxt-link>
          <nuxt-link to="/profiledemo/compProfile" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
            active-class="border-yellow-500">Company Info</nuxt-link>
        </div>
        <div class="flex flex-col-reverse justify-between gap-6 md:flex-row md:items-center">
        <div class="flex items-center">
          <Profile />
        </div>
      </div>
      </div>
    </nav>
   

    <!-- Profile Form -->
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
        <Personal />
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