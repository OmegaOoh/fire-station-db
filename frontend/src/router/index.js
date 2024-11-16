import {createRouter, createWebHistory } from 'vue-router'
import RecordStats from '@/views/RecordStats.vue'
import RecordFinder from '@/views/RecordFinder.vue'
import RecordCreator from '@/views/RecordCreator.vue'

const routes = [
    {
        path: '/',
        name: 'Overview',
        component: RecordStats,
    },
    {
        path: '/create',
        name: "Creator",
        component: RecordCreator,
    },
    {
        path: '/find',
        name: 'finder',
        component: RecordFinder,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;