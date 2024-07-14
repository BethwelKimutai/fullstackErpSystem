<template>
    <ul class="relative flex flex-col gap-2 max-w-[280px] mx-auto mt-24 z-20">
      <li>
        <details class="group relative">
          <summary class="flex items-center justify-between gap-2 p-2 font-medium marker:content-none hover:cursor-pointer">
            <span class="flex gap-2">
              <img class="w-6 h-6 rounded-lg" src="https://lh3.googleusercontent.com/a/AGNmyxbSlMgTRzE3_SMIxpDAhpNad-_CN5_tmph1NQ1KhA=s96-c" alt="">
              <span>{{ user }}</span>
            </span>
            <svg class="w-5 h-5 text-gray-500 transition group-open:rotate-90" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"></path>
            </svg>
          </summary>
  
          <article class="absolute right-0 mt-2 px-4 pb-4 bg-white border rounded shadow-lg z-50">
            <ul class="flex flex-col gap-4 pl-2 mt-4">
              <li class="flex gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"></path>
                </svg>
                <a href="http://127.0.0.1:8000/user/dashboard">Dashboard</a>
              </li>
              <li class="flex gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z"></path>
                </svg>
                <a href="http://127.0.0.1:8000/user/study-lists">Study Lists</a>
              </li>
              <li class="flex gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m6.75 12l-3-3m0 0l-3 3m3-3v6m-1.5-15H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"></path>
                </svg>
                <a href="http://127.0.0.1:8000/user/contribution">Your contribution</a>
              </li>
              <li class="flex gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M10.343 3.94c.09-.542.56-.94 1.11-.94h1.093c.55 0 1.02.398 1.11.94l.149.894c.07.424.384.764.78.93.398.164.855.142 1.205-.108l.737-.527a1.125 1.125 0 011.45.12l.773.774c.39.389.44 1.002.12 1.45l-.527.737c-.25.35-.272.807-.108 1.205.165.396.506.71.93.78l.894.149c.542.09.94.56.94 1.11v1.094c0 .55-.398 1.02-.94 1.11l-.894.149c-.424.07-.764.384-.93.78-.164.398-.142.855.108 1.205l.527.737c.414.58.336 1.38-.12 1.45l-.774.773c-.389.39-1.002.44-1.45.12l-.737-.527c-.35-.25-.807-.272-1.205-.108-.396.165-.71.506-.78.93l-.149.894c-.09.542-.56.94-1.11.94h-1.094c-.55 0-1.02-.398-1.11-.94l-.149-.894c-.07-.424-.384-.764-.78-.93-.398-.164-.855-.142-1.205.108l-.737.527a1.125 1.125 0 01-1.45-.12l-.773-.774a1.125 1.125 0 01-.12-1.45l.527-.737c.25-.35.272-.807.108-1.205-.165-.396-.506-.71-.93-.78l-.894-.149c-.542-.09-.94-.56-.94-1.11v-1.094c0-.55.398-1.02.94-1.11l.894-.149c.424-.07.764-.384.93-.78.164-.398.142-.855-.108-1.205l-.527-.737a1.125 1.125 0 01.12-1.45l.774-.773a1.125 1.125 0 011.45-.12l.737.527c.35.25.807.272 1.205.108.396-.165.71-.506.78-.93l.149-.894z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15 12.75a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <a href="http://127.0.0.1:8000/user/settings">Settings</a>
              </li>
              <li class="flex gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-3a2.25 2.25 0 00-2.25 2.25V9m0 12H15.75m-9.75-7.5h15m-15 0a2.25 2.25 0 012.25 2.25v6A2.25 2.25 0 006.75 21h-3A2.25 2.25 0 001.5 18.75v-6A2.25 2.25 0 003.75 12h3zm15 0a2.25 2.25 0 012.25 2.25v6a2.25 2.25 0 01-2.25 2.25h-3A2.25 2.25 0 0113.5 18.75v-6A2.25 2.25 0 0115.75 12h3z"></path>
                </svg>
                <button @click="logout" class="text-red-500 text-sm px-2 py-1 hover:bg-red-200 rounded-md">Logout</button>
              </li>
            </ul>
          </article>
        </details>
      </li>
    </ul>
  </template>
  
  <script>
  import { defineComponent, ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    setup() {
      const user = ref('');
      const message = ref('');
      const router = useRouter();
  
      const checkAuthentication = async () => {
        try {
          const response = await fetch('http://127.0.0.1:8000/jikoTrack/getCompany', {
            method: "GET",
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
          });
  
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
  
          const content = await response.json();
          user.value = content.name;
          window.dispatchEvent(new CustomEvent('auth', { detail: true }));
        } catch (e) {
          await router.push('/Signup/loginCompany');
          window.dispatchEvent(new CustomEvent('auth', { detail: false }));
        }
      };
  
      onMounted(checkAuthentication);
  
      const logout = async () => {
        try {
          await fetch('http://localhost:8000/jikoTrack/logout', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
          });
  
          await router.push('/Signup/loginCompany');
        } catch (error) {
          console.error('Error during logout:', error);
        }
      };
  
      return {
        user,
        message,
        logout,
      };
    },
    beforeRouteEnter(to, from, next) {
      fetch('http://127.0.0.1:8000/jikoTrack/getCompany', {
        method: "GET",
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(content => {
          next();
        })
        .catch(error => {
          next('/Signup/loginCompany');
        });
    },
  });
  </script>
  
<style scoped>
.group summary {
  list-style: none;
}

.group[open] summary ~ article {
  display: block;
}

.group summary ~ article {
  display: none;
}
</style>
  