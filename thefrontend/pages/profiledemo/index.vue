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
<<<<<<< HEAD
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
=======
          <nuxt-link to="/profiledemo/personalinfo" class="px-4 py-2 text-black hover:text-yellow-800 border-b-2"
            active-class="border-yellow-500">Personal Info</nuxt-link>
        </div>
      </div>
    </nav>

    <!-- Profile Form -->
    <div class="bg-white p-8 rounded-lg shadow-md mt-4 mx-auto max-w-4xl">
      <form>
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Profile</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">This information will be displayed publicly so be careful
              what you share.</p>

            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div class="sm:col-span-4">
                <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
                <div class="mt-2">
                  <div
                    class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <span class="flex select-none items-center pl-3 text-gray-500 sm:text-sm">workcation.com/</span>
                    <input type="text" name="username" id="username" autocomplete="username"
                      class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
                      placeholder="janesmith" />
                  </div>
                </div>
              </div>

              <div class="col-span-full">
                <label for="about" class="block text-sm font-medium leading-6 text-gray-900">About</label>
                <div class="mt-2">
                  <textarea id="about" name="about" rows="3"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                </div>
                <p class="mt-3 text-sm leading-6 text-gray-600">Write a few sentences about yourself.</p>
              </div>

              <div class="col-span-full">
                <label for="photo" class="block text-sm font-medium leading-6 text-gray-900">Photo</label>
                <div class="mt-2 flex items-center gap-x-3">
                  <UserCircleIcon class="h-12 w-12 text-gray-300" aria-hidden="true" />
                  <button type="button"
                    class="rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Change</button>
                </div>
              </div>

              <div class="col-span-full">
                <label for="cover-photo" class="block text-sm font-medium leading-6 text-gray-900">Cover photo</label>
                <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                  <div class="text-center">
                    <PhotoIcon class="mx-auto h-12 w-12 text-gray-300" aria-hidden="true" />
                    <div class="mt-4 flex text-sm leading-6 text-gray-600">
                      <label for="file-upload"
                        class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500">
                        <span>Upload a file</span>
                        <input id="file-upload" name="file-upload" type="file" class="sr-only" />
                      </label>
                      <p class="pl-1">or drag and drop</p>
                    </div>
                    <p class="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit"
            class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </form>
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356
    </div>
  </div>
</template>
<script>
<<<<<<< HEAD

=======
definePageMeta({
  layout: 'home'
})
>>>>>>> e5ef20e6faa5594b57c646fde9c033923d255356
</script>

<style scoped>
.router-link-exact-active {
  color: rgb(251 191 36);
}
</style>