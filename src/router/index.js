import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Login from '../views/Login.vue'
import Dashboard from '../views/dashboard.vue'
import store from '../store'
import VueEllipseProgress from 'vue-ellipse-progress'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueEllipseProgress)
Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    beforeEnter (to, from, next) {
      if (store.getters.isAuthenticated) {
        next()
      } else {
        // store.dispatch('try_auto_login', to.fullPath)
        next('/login')
      }
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
