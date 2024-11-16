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
                <div class="collapse-title text-xl font-medium">{{ staffData.name }}, {{ staffData.station }}
                    <div class="badge badge-secondary" v-if="staffData.fire_fighter_rank">Fire Fighter</div>
                </div>
                <div class="collapse-content grid grid-cols-1 md:grid-cols-2">
                    <p><strong>Date of Birth:</strong> {{ staffData.dob }}</p>
                    <p><strong>Gender:</strong> {{ staffData.gender }}</p>
                    <p><strong>Position:</strong> {{ staffData.position }}</p>
                    <p v-if="staffData.fire_fighter_rank"><strong>Fire Fighter Rank:</strong> {{ staffData.fire_fighter_rank }}</p>
                    <p v-if="staffData.fire_fighter_role"><strong>Fire Fighter Role:</strong> {{ staffData.fire_fighter_role }}</p>
                    <p v-if="staffData.responded"><strong>Dispatch Responded: </strong> {{ staffData.responded }}</p>
                    <ul class="col-span-2 grid grid-cols-1 md:grid-cols-6"><strong class="col-span-6">
                        Shifts:
                    </strong>
                        <li v-for="(shift, index) in staffData.shift" :key="index">
                            {{ shift.day }} {{ shift.shift_start }} - {{ shift.shift_end }}
                        </li>
                    </ul>
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
            station: "Main Fire Station",
            shift: [
                { day: "Monday", shift_start: "09:00", shift_end: "17:00" },
                { day: "Wednesday", shift_start: "09:00", shift_end: "17:00" }
            ],
            fire_fighter_rank: "Firefighter",
            fire_fighter_role: "Incident Commander",
            responded: 10
        },
        {
            name: "Jane Smith",
            dob: "1990-06-25",
            gender: "Female",
            position: "Paramedic",
            station: "Downtown Fire Station",
            shift: [
                { day: "Tuesday", shift_start: "09:00", shift_end: "17:00" },
                { day: "Thursday", shift_start: "09:00", shift_end: "17:00" }
            ],
            fire_fighter_rank: null,
            fire_fighter_role: null,
        },
        {
            name: "Alice Johnson",
            dob: "1988-01-30",
            gender: "Female",
            position: "Engineer",
            station: "Northside Fire Station",
            shift: [
                { day: "Wednesday", shift_start: "09:00", shift_end: "17:00" },
                { day: "Friday", shift_start: "09:00", shift_end: "17:00" }
            ],
            fire_fighter_rank: "Engineer",
            fire_fighter_role: "Medical Technician",
            responded: 1
        },
        {
            name: "Bob Brown",
            dob: "1975-11-05",
            gender: "Male",
            position: "Lieutenant",
            station: "Main Fire Station",
            shift: [
                { day: "Thursday", shift_start: "09:00", shift_end: "17:00" },
                { day: "Saturday", shift_start: "09:00", shift_end: "17:00" }
            ],
            fire_fighter_rank: "Lieutenant",
            fire_fighter_role: "Company Officer",
            responded: 2
        },
        {
            name: "Charlie Black",
            dob: "1995-09-15",
            gender: "Male",
            position: "Firefighter",
            station: "Downtown Fire Station",
            shift: [
                { day: "Saturday", shift_start: "09:00", shift_end: "17:00" },
                { day: "Sunday", shift_start: "09:00", shift_end: "17:00" }
            ],
            fire_fighter_rank: "Firefighter",
            fire_fighter_role: "Search and Rescue Technician",
            responded: 5,
        },
        {
            name: "Diana Prince",
            dob: "1983-04-20",
            gender: "Female",
            position: "Captain",
            station: "Northside Fire Station",
            shift: [
                { day: "Monday", shift_start: "08:00", shift_end: "16:00" },
                { day: "Tuesday", shift_start: "08:00", shift_end: "16:00" }
            ],
            fire_fighter_rank: "Captain",
            fire_fighter_role: "Operations Officer",
            responded: 23,
        },
        {
            name: "Ethan Hunt",
            dob: "1980-12-12",
            gender: "Male",
            position: "Firefighter",
            station: "Main Fire Station",
            shift: [
                { day: "Friday", shift_start: "09:00", shift_end: "17:00" },
                { day: "Saturday", shift_start: "09:00", shift_end: "17:00" }
            ],
            fire_fighter_rank: "Firefighter",
            fire_fighter_role: "Hazmat Technician",
            responded: 5,
        }
    ];
}

const filteredStaff = computed(() => {
    return staff.value.filter(staff => {
            let matched = staff.name.toLowerCase().includes(search.value.toLowerCase()) ||
                staff.position.toLowerCase().includes(search.value.toLowerCase()) ||
                staff.station.toLowerCase().includes(search.value.toLowerCase())
            if (staff.fire_fighter_rank && staff.fire_fighter_role) {
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