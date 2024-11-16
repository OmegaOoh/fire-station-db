<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl mb-4">
            Staff
        </h2>
        
        <template v-for="(staffData, index) in staff" :key="index">
            <div class="collapse collapse-arrow bg-base-300 mb-4">
                <input type="radio" name="my-accordion-2" checked="checked" />
                <div class="collapse-title text-xl font-medium">{{index + 1}}. {{ staffData.name }}, {{ staffData.station }}
                    <div class="badge badge-secondary" v-if="staffData.fire_fighter_rank">Fire Fighter</div>
                </div>
                    <div class="collapse-content grid grid-cols-1 md:grid-cols-2">
                        <p><strong>Date of Birth:</strong> {{ staffData.dob }}</p>
                        <p><strong>Gender:</strong> {{ staffData.gender }}</p>
                        <p><strong>Position:</strong> {{ staffData.position }}</p>
                        <p><strong>Shift:</strong> {{ staffData.shift }}</p>
                        <p v-if="staffData.fire_fighter_rank"><strong>Fire Fighter Rank:</strong> {{ staffData.fire_fighter_rank }}</p>
                        <p v-if="staffData.fire_fighter_role"><strong>Fire Fighter Role:</strong> {{ staffData.fire_fighter_role }}</p>
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
import { ref, onMounted } from 'vue'
console.log(apiClient)

const staff = ref([])

const fetchStaffs = async() => {
    /*
        const response = await apiClient.get(`/staff/`)
        staff.value = response.data
    */
   //Placeholder Data
    staff.value = [
        {
            name: "John Doe",
            dob: "1985-04-12",
            gender: "Male",
            position: "Firefighter",
            station: "Station A",
            shift: "Mon 09:00 - 16:00",
            fire_fighter_rank: "Firefighter",
            fire_fighter_role: "Incident Commander"
        },
        {
            name: "Jane Smith",
            dob: "1990-06-25",
            gender: "Female",
            position: "Paramedic",
            station: "Station B",
            shift: "Tue 09:00 - 16:00",
            fire_fighter_rank: null,
            fire_fighter_role: null
        },
        {
            name: "Alice Johnson",
            dob: "1988-01-30",
            gender: "Female",
            position: "Engineer",
            station: "Station C",
            shift: "Wed 09:00 - 16:00",
            fire_fighter_rank: "Engineer",
            fire_fighter_role: "Medical Technician"
        },
        {
            name: "Bob Brown",
            dob: "1975-11-05",
            gender: "Male",
            position: "Lieutenant",
            station: "Station A",
            shift: "Thu 09:00 - 16:00",
            fire_fighter_rank: "Lieutenant",
            fire_fighter_role: "Company Officer"
        },
        {
            name: "Charlie Black",
            dob: "1995-09-15",
            gender: "Male",
            position: "Firefighter",
            station: "Station B",
            shift: "Sat 09:00 - 16:00",
            fire_fighter_rank: "Firefighter",
            fire_fighter_role: "Search and Rescue Technician"
        }
    ];
}

onMounted(() => {
    fetchStaffs();
})


</script>