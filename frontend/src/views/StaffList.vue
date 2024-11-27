<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl mb-4">
            Staff
        </h2>

        <label class="mb-4">
            <div class="label-text-alt">
                <span class="label-text-alt">
                    <label>
                        <span class="label-text ">Only Fire Fighter? </span>
                        <input v-model="filterFighter" type="checkbox" :checked="filterFighter" class="checkbox checkbox-sm">
                    </label>
                </span>
            </div>
            <input 
                type="text" 
                v-model="search" 
                placeholder="Search Staff..." 
                class="input input-bordered w-full mb-2" 
            />
        </label>
        
        <template v-for="staffData in filteredStaff" :key="staffData.id">
            <div class="collapse collapse-arrow bg-base-300 mb-4">
                <input type="radio" name="my-accordion-2" checked="checked" />
                <div class="collapse-title text-xl font-medium">{{ staffData.full_name }}, {{ staffData.station_name }}
                    <div class="badge badge-secondary" v-if="staffData.is_fire_fighter">Fire Fighter</div>
                </div>
                <div class="collapse-content grid grid-cols-1 md:grid-cols-2">
                    <p><strong>Date of Birth:</strong> {{ staffData.dob }}</p>
                    <p><strong>Gender:</strong> {{ staffData.gender }}</p>
                    <p><strong>Position:</strong> {{ staffData.position }}</p>
                    <div v-if="staffData.is_fire_fighter">
                        <p v-if="staffData.firefighter_detail.rank"><strong>Fire Fighter Rank:</strong> {{ staffData.firefighter_detail.rank }}</p>
                        <p v-if="staffData.firefighter_detail.role"><strong>Fire Fighter Role:</strong> {{ staffData.firefighter_detail.role }}</p>
                        <p v-if="staffData.firefighter_detail.responded"><strong>Dispatch Responded: </strong> {{ staffData.responded }}</p>
                    </div>
                    <ul class="col-span-2 grid grid-cols-1 md:grid-cols-6"><strong class="col-span-6">
                        Shifts:
                    </strong>
                        <li v-for="(shift, index) in staffData.shift_detail" :key="index">
                            {{ shift.day }} {{ shift.shift_start.slice(0, 5) }} - {{ shift.shift_end.slice(0, 5) }}
                        </li>
                    </ul>
                    <div></div>
                    <div class="flex justify-end w-full">
                        <router-link class="btn btn-accent w-fit" :to="`/staff/${staff.id}/edit/`">Edit</router-link>
                    </div>
                    
                </div>
            </div>
        </template>
    </div>

    <RouterLink class="btn btn-primary text-4xl pb-2 btn-square absolute z-10 bottom-4 right-4 btn-lg" to="/staff/add">
        +
    </RouterLink>
</template>

<script setup>
import apiClient from '@/api.js'
import { ref, onMounted, computed } from 'vue'
console.log(apiClient)

const staff = ref([])
const search = ref('')
const filterFighter = ref(false)

const fetchStaffs = async() => {
    
    const res = await apiClient.get(`/fire-station/staff/`)
    staff.value = res.data
}

const filteredStaff = computed(() => {
    return staff.value.filter(staff => {
            let matched = staff.full_name.toLowerCase().includes(search.value.toLowerCase()) ||
                staff.position.toLowerCase().includes(search.value.toLowerCase()) ||
                staff.station.toLowerCase().includes(search.value.toLowerCase())
            if (staff.is_fire_fighter) {
                matched = matched ||
                        staff.fire_fighter_rank.toLowerCase().includes(search.value.toLowerCase()) ||
                        staff.fire_fighter_role.toLowerCase().includes(search.value.toLowerCase())
            } else {
                if (filterFighter.value) {
                    matched = false;
                }
            }

        return matched
    });
});

onMounted(() => {
    fetchStaffs();
})


</script>