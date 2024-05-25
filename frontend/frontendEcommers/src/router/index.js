import {crateRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
    
        name: 'About',
    
        component: () => import('../views/About.vue')}/// se mueve para otra vista
]

const router = crateRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
}) 

export default router