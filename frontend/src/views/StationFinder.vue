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

const fetchStation = async() => {
    const response = await apiClient.get('/fire-station/')
    stations.value = response.data;
}

onMounted(() => {
    fetchStation()
}) 

</script>