import { ref } from 'vue';

export const useUser = () => {
  const user = ref({
    role: null,
  });

  const setUser = (newUser) => {
    user.value = newUser;
  };

  return {
    user,
    setUser,
  };
};