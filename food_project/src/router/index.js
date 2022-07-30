import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/paginas/home.vue';
import Admin from '../components/paginas/admin.vue';
import Recetas from '../components/paginas/recetas.vue';
import Curiosidades from '../components/paginas/curiosidades.vue';
import Receta from '../components/paginaReceta.vue';
import Login from '../components/paginas/login.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/admin',
    name: 'admin',
    component: Admin
  },
  {
    path: '/recetas',
    name: 'recetas',
    component: Recetas
  },
  {
    path: '/curiosidades',
    name: 'curiosidades',
    component: Curiosidades
  },
  {
    path: '/receta/:id',
    name: 'receta',
    component: Receta
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
