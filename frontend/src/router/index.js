import {createRouter, createWebHistory } from 'vue-router'
import RecordStats from '@/views/RecordStats.vue'
import RecordFinder from '@/views/RecordFinder.vue'
import RecordCreate from '@/views/RecordCreate.vue'
import RecordEdit from '@/views/RecordEdit.vue'
import StationFinder from '@/views/StationFinder.vue'
import StaffCreate from '@/views/StaffCreate.vue'
import StationCreate from '@/views/StationCreate.vue'
import StaffList from '@/views/StaffList.vue'
import StationDetail from '@/views/StationDetail.vue'
import ItemCreate from '@/views/ItemCreate.vue'
import StaffEdit from '@/views/StaffEdit.vue'
import ShiftManager from '@/views/ShiftManager.vue'

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
        path: '/:id/edit',
        name: 'edit',
        component: RecordEdit,
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
        path:'/station/:id/manage',
        name: 'addItem',
        component: ItemCreate,
    },
    {
        path:'/staff',
        name: 'staffIndex',
        component: StaffList,
    },
    {
        path: '/staff/:id/edit',
        name: 'staffEdit',
        component: StaffEdit,
    },
    {
        path:'/staff/add',
        name: 'staffCreate',
        component: StaffCreate,
    },
    {
        path:'/shift',
        name: 'shift',
        component: ShiftManager,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;