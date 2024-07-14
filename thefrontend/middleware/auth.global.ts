import { defineNuxtRouteMiddleware, navigateTo } from '#app';
import { useAuthStore } from '@/stores/auth';

export default defineNuxtRouteMiddleware((to) => {
  const authStore = useAuthStore();
  const { authenticated, auth_user } = authStore;

  // If user is authenticated and tries to access the login page, redirect to homepage
  if (to.path === '/login' && authenticated) {
    return navigateTo('/');
  }

  // If user is not authenticated or auth_user is null/empty, redirect to homepage
  if (!authenticated || !auth_user || Object.keys(auth_user).length === 0) {
    if (to.path !== '/') {
      return navigateTo('/');
    }
  }
});
