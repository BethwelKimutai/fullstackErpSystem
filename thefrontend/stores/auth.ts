import { defineStore } from "pinia";
import { useCookie } from 'nuxt/app'; 

interface UserPayloadInterface {
  username: string;
  password: string;
}

export const useAuthStore = defineStore("auth", {
  state: () => ({
    authenticated: false,
    auth_user: {
      is_superuser: false,
      is_accounting_manager: false,
      is_manager: false,
      is_inventory_manager: false,
      is_purchase_manager: false,
    },
    user_id: "",
  }),
  actions: {
    async authenticateUser({ username, password }: UserPayloadInterface) {
      const { data, pending }: any = await useFetch(
        "http://127.0.0.1:8000/backend/users/login/",
        {
          method: "post",
          headers: { "Content-Type": "application/json" },
          credentials: 'include',
          body: {
            username,
            password,
          },
        }
      );

      if (data.value.code == "200") {
        const jwt = useCookie("token");
        jwt.value = data.value.jwt;
        this.authenticated = true;
      }
    },
    async profileUser() {
      const token = useCookie("token");
      const router = useRouter();
      const { data, pending }: any = await useFetch(
        "http://127.0.0.1:8000/backend/users/getuser/",
        {
          method: "post",
          headers: { "Content-Type": "application/json" },
          credentials: 'include',
          body: {
            token: token,
          },
        }
      );

      if (data.value.code == "200") {
        this.auth_user = data.value.user;
        if (String(this.auth_user) != '{}') {
          const { is_superuser, is_manager, is_accounting_manager, is_inventory_manager, is_purchase_manager } = this.auth_user;
          if (is_superuser) {
            router.push('/superuser');
          } else if (is_manager) {
            router.push('/home/manager');
          } else if (is_accounting_manager) {
            router.push('/accounting');
          } else if (is_inventory_manager) {
            router.push('/inventory');
          } else if (is_purchase_manager) {
            router.push('/purchase');
          } else {
            router.push('/');
          }
        }
      }
    },
    logout() {
      const jwt = useCookie("token");
      jwt.value = null;
      this.authenticated = false;
      this.auth_user = {
        is_superuser: false,
        is_accounting_manager: false,
        is_manager: false,
        is_inventory_manager: false,
        is_purchase_manager: false,
      };
      this.user_id = "";
      const router = useRouter();
      router.push('/');
    },
  },
  getters: {
    getUserProfile(state) {
      return this.auth_user;
    },
  },
  persist: true,
});
