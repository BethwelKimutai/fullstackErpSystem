import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    jwt: null, // JWT token
    userDetails: null, // User details
  }),
  actions: {
    setJwt(token) {
      this.jwt = token;
    },
    setUserDetails(userDetails) {
      this.userDetails = userDetails;
    },
    clearAuth() {
      this.jwt = null;
      this.userDetails = null;
      document.cookie = 'jwt=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    },
    async fetchUserDetails() {
      const jwtToken = this.jwt;
      if (!jwtToken) {
        throw new Error('JWT token not found');
      }
      try {
        const response = await fetch('http://127.0.0.1:8000/backend/users/getuser/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json' 
          },
        });
        if (response.ok) {
          const data = await response.json();
          if (data) {
            this.setUserDetails(data);
          } else {
            throw new Error('User details not found');
          }
        } else {
          const errorData = await response.json();
          throw new Error(errorData.detail || 'Error fetching user details');
        }
      } catch (error) {
        console.error('Error fetching user details:', error);
        throw error;
      }
    },
  },
});
