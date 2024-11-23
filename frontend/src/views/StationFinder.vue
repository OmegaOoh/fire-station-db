<template>
    <div class="px-4 pt-4">
        <h1 class="text-4xl font-bold mb-6">Fire Stations</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            <div 
                v-for="station in stations" 
                :key="station.id" 
                class="card bg-base-200 shadow-md p-2"
            >
                <div class="card-body">
                    <h2 class="card-title text-2xl">{{ station.station_name }}</h2>
                    <p><strong>Address:</strong> {{ station.address }}</p>
                    <p><strong>Staff Capacity:</strong> {{ station.staff_capacity }}</p>
                    <p><strong>Fire Engine Capacity:</strong> {{ station.fire_engine_capacity }}</p>
                    <div class="card-actions justify-end">
                        <router-link 
                            :to="`/station/${station.id}`"
                            class="btn btn-primary"
                        >
                            View Details
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <RouterLink class="btn btn-primary text-4xl pb-2 btn-square absolute z-10 bottom-4 right-4 btn-lg" to="/station/add">
        +
    </RouterLink>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import apiClient from '@/api.js' 
const stations = ref([]);
//     {
//         id: 1,
//         station_name: 'Main Fire Station',
//         address: '123 Main St, Springfield',
//         staff_capacity: 20,
//         fire_engine_capacity: 5
//     },
//     {
//         id: 2,
//         station_name: 'Downtown Fire Station',
//         address: '456 Elm St, Springfield',
//         staff_capacity: 15,
//         fire_engine_capacity: 3
//     },
//     {
//         id: 3,
//         station_name: 'Northside Fire Station',
//         address: '789 Oak St, Springfield',
//         staff_capacity: 10,
//         fire_engine_capacity: 2
//     },
//     {
//         id: 4,
//         station_name: 'Westside Fire Station',
//         address: '321 Pine St, Springfield',
//         staff_capacity: 18,
//         fire_engine_capacity: 4
//     }
// ]);

const fetchStation = async() => {
    const response = await apiClient.get('/fire-station/')
    stations.value = response.data;
}

onMounted(() => {
    fetchStation()
}) 

</script>