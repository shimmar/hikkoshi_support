import { createRouter, createWebHistory } from 'vue-router'
import SelectConditions from '../views/SelectConditions.vue'
import ListRooms from '../views/ListRooms.vue'
import ShowResult from '../views/ShowResult.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'select_conditions',
      component: SelectConditions
    },
    {
      path: '/list',
      name: 'list',
      component: ListRooms
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
    },
    {
      path: '/result',
      name: 'result',
      component: ShowResult
    }
  ]
})

export default router
