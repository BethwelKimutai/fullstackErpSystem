import { createRouter, createWebHistory } from 'vue-router'
import UserList from '@/views/UserList.vue'
import UserDetails from '@/views/UserDetails.vue'
import LoginCompany from '@/views/LoginCompany.vue'

const routes = [
  {
    path: '/',
    name: 'UserList',
    component: UserList
  },
  {
    path: '/user-details/:id',
    name: 'UserDetails',
    component: UserDetails
  },
  {
    path: '/Signup/loginCompany',
    name: 'LoginCompany',
    component: LoginCompany
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
