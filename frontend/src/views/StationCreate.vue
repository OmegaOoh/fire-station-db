<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl">Create Station</h2>
        <form ref="stationForm" @submit.prevent="submitData" class="my-4 grid grid-col-1 md:grid-cols-2 gap-20 w-full">
            <label class="form-control w-full col-span-2">
                    <div class="label">
                        <span class="label-text text-xl">Station name:</span>
                    </div>
                <input 
                    v-model="station.name" 
                    type="text" 
                    id="name" 
                    name="name" 
                    class="input input-bordered rounded-md ml-4 w-full" 
                    required
                />
            </label>
            <label class="form-control w-full col-span-2">
                    <div class="label">
                        <span class="label-text text-xl">Address:</span>
                    </div>
                <input 
                    v-model="station.address" 
                    type="text" 
                    id="address" 
                    name="address" 
                    class="input input-bordered rounded-md ml-4 w-full" 
                    required
                />
            </label>
            <label class="form-control w-full">
                    <div class="label">
                        <span class="label-text text-xl">Staff Capacity:</span>
                    </div>
                    <input 
                    v-model="station.staff_capacity" 
                    type="number" 
                    id="staff_capacity" 
                    name="staff_capacity" 
                    class="input input-bordered rounded-md ml-4 w-full" 
                    :min = 1
                    required
                />
            </label>
            <label class="form-control w-full">
                    <div class="label">
                        <span class="label-text text-xl">Engine Capacity:</span>
                    </div>
                    <input 
                    v-model="station.engine_capacity" 
                    type="number" 
                    id="engine_capacity" 
                    name="engine_capacity" 
                    class="input input-bordered rounded-md ml-4 w-full" 
                    :min = 1
                    required
                />
            </label>
            <button type="submit" class="btn btn-primary col-span-2">Submit</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import apiClient from '@/api.js';
import { useRouter } from 'vue-router';

const router = useRouter();
const station = ref({
    name: '',
    address: '',
    staff_capacity: null,
    fire_engine_capacity: null
});

const submitData = async () => {
    try {
        await apiClient.post('/station/', station.value);
        console.log(station.value)
    } catch (error) {
        console.error('Error creating station:', error);
    }
    router.push('/stations');
};
</script>