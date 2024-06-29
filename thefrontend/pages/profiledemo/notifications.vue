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
    <div class="bg-white p-8 rounded-lg shadow-md mt-4 mx-auto max-w-4xl">
      <form>
        <div class="border-b border-gray-900/10 pb-12">
          <h2 class="text-base font-semibold leading-7 text-gray-900">Notifications</h2>
          <p class="mt-1 text-sm leading-6 text-gray-600">We'll always let you know about important changes, but you
            pick
            what else you want to hear about.</p>

          <div class="mt-10 space-y-10">
            <fieldset>
              <legend class="text-sm font-semibold leading-6 text-gray-900">By Email</legend>
              <div class="mt-6 space-y-6">
                <div class="relative flex gap-x-3">
                  <div class="flex h-6 items-center">
                    <input id="comments" name="comments" type="checkbox"
                      class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="text-sm leading-6">
                    <label for="comments" class="font-medium text-gray-900">Comments</label>
                    <p class="text-gray-500">Get notified when someones posts a comment on a posting.</p>
                  </div>
                </div>
                <div class="relative flex gap-x-3">
                  <div class="flex h-6 items-center">
                    <input id="candidates" name="candidates" type="checkbox"
                      class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="text-sm leading-6">
                    <label for="candidates" class="font-medium text-gray-900">Candidates</label>
                    <p class="text-gray-500">Get notified when a candidate applies for a job.</p>
                  </div>
                </div>
                <div class="relative flex gap-x-3">
                  <div class="flex h-6 items-center">
                    <input id="offers" name="offers" type="checkbox"
                      class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="text-sm leading-6">
                    <label for="offers" class="font-medium text-gray-900">Offers</label>
                    <p class="text-gray-500">Get notified when a candidate accepts or rejects an offer.</p>
                  </div>
                </div>
              </div>
            </fieldset>
            <fieldset>
              <legend class="text-sm font-semibold leading-6 text-gray-900">Push Notifications</legend>
              <p class="mt-1 text-sm leading-6 text-gray-600">These are delivered via SMS to your mobile phone.</p>
              <div class="mt-6 space-y-6">
                <div class="flex items-center gap-x-3">
                  <input id="push-everything" name="push-notifications" type="radio"
                    class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  <label for="push-everything"
                    class="block text-sm font-medium leading-6 text-gray-900">Everything</label>
                </div>
                <div class="flex items-center gap-x-3">
                  <input id="push-email" name="push-notifications" type="radio"
                    class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  <label for="push-email" class="block text-sm font-medium leading-6 text-gray-900">Same as
                    email</label>
                </div>
                <div class="flex items-center gap-x-3">
                  <input id="push-nothing" name="push-notifications" type="radio"
                    class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  <label for="push-nothing" class="block text-sm font-medium leading-6 text-gray-900">No push
                    notifications</label>
                </div>
              </div>
            </fieldset>
          </div>
        </div>
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit"
            class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import Profile from '/components/Profile.vue';

export default{
  components :{
    Profile,
  }

};

</script>

<style scoped>
.router-link-exact-active {
  color: rgb(251 191 36);
}
</style>