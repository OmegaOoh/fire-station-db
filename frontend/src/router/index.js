import {createRouter, createWebHistory } from 'vue-router'
import RecordStats from '@/views/RecordStats.vue'
import RecordFinder from '@/views/RecordFinder.vue'
import RecordCreate from '@/views/RecordCreate.vue'
import StationFinder from '@/views/StationFinder.vue'
import StaffCreate from '@/views/StaffCreate.vue'
import StationCreate from '@/views/StationCreate.vue'
import StaffList from '@/views/StaffList.vue'
import StationDetail from '@/views/StationDetail.vue'
import ItemCreate from '@/views/ItemCreate.vue'

const routes = [
    {
        path: '/',
        name: 'Overview',
        component: RecordStats,
    },
    {
        path: '/create',
        name: "recordCreate",
        component: RecordCreate,
    },
    {
        path: '/find',
        name: 'finder',
        component: RecordFinder,
    },
    {
        path:'/station',
        name: 'stationFinder',
        component: StationFinder,
    },
    {
        path:'/station/add',
        name: 'stationCreate',
        component: StationCreate,
    },
    {
        path:'/station/:id',
        name: 'stationDetail',
        component: StationDetail,
    },
    {
        path:'/station/:id/add',
        name: 'addItem',
        component: ItemCreate,
    },
    {
        path:'/staff',
        name: 'staffIndex',
        component: StaffList,
    },
    {
        path:'/staff/add',
        name: 'staffCreate',
        component: StaffCreate,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;