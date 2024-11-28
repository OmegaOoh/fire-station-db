<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">Dispatch Index</h1>
        
        <div class="mb-4">
            <input 
                type="text" 
                v-model="search" 
                placeholder="Search dispatches..." 
                class="input input-bordered w-full mb-2" 
            />
        </div>

        <div class="mb-4">
            <router-link to="/dispatch/create" class="btn btn-primary">Create New Dispatch</router-link>
        </div>

        <table class="table w-full">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Incident Type</th>
                    <th>Address</th>
                    <th>Station</th>
                    <th>Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="dispatch in filteredDispatches" :key="dispatch.id">
                    <td>{{ dispatch.id }}</td>
                    <td>{{ dispatch.incident }}</td>
                    <td>{{ dispatch.address }}</td>
                    <td>{{ dispatch.station }}</td>
                    <td>{{ formatDate(dispatch.reported_time) }}</td>
                    <td>
                        <router-link :to="`/${dispatch.id}/edit`" class="btn btn-secondary btn-sm">Edit</router-link>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import apiClient from '@/api';
import { ref, computed, onMounted } from 'vue';
import { RouterLink } from 'vue-router';

//const router = useRouter();

const dispatches = ref([]);

const search = ref('');

const filteredDispatches = computed(() => {
    return dispatches.value.filter(dispatch => {
        return (
            dispatch.incident.toLowerCase().includes(search.value.toLowerCase()) ||
            dispatch.address.toLowerCase().includes(search.value.toLowerCase()) ||
            dispatch.station.toLowerCase().includes(search.value.toLowerCase())
        );
    });
});

const formatDate = (date) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString(undefined, options);
};

const fetchdata = async() => {
    const res = await apiClient.get(`/fire-station/dispatch/`)
    dispatches.value = res.data
}

onMounted(
    () => {
        fetchdata()
    }
)
</script>