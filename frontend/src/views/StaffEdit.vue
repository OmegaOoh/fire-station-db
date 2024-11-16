<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl">
            {{ staff.name }}
        </h2>
        <form ref="staffForm" @submit.prevent="submitData" class="my-4 grid grid-col-1 md:grid-cols-2 gap-20 w-full">
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Full Name</span>
                </div>
                <input v-model="staff.name" class="input input-bordered rounded-md ml-4 w-full" type="text" required>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Date of Birth</span>
                </div>
                <input v-model="staff.dob" class="input input-bordered rounded-md ml-4 w-full" type="date" required>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Gender</span>
                </div>
                <select v-model="staff.gender" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Gender</option>
                    <option v-for="(gender, index) in choices.gender" :key="index">
                        {{ gender }}
                    </option>
                </select>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Position</span>
                </div>
                <input v-model="staff.position" class="input input-bordered rounded-md ml-4 w-full" type="text" required>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Station</span>
                </div>
                <select v-model="staff.station" class="select select-bordered ml-4 w-full" required>
                    <option disabled selected>Station</option>
                    <option v-for="(station, index) in choices.station" :key="index">
                        {{ station }}
                    </option>
                </select>
            </label>
            <div class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Shifts</span>
                </div>
                <div class="ml-4 grid grid-cols-2">
                    <div v-for="(shift, index) in choices.shift" :key="index" class="flex items-center mb-2">
                        <input type="checkbox" :id="'shift-' + index" v-model="staff.shift" :value="shift" class="checkbox" />
                        <label :for="'shift-' + index" class="ml-2">{{ shift }}</label>
                    </div>
                </div>
            </div>

            <div class="form-control">
                <label class="label cursor-pointer">
                    <span class="label-text text-xl">Fire Fighter?</span>
                    <input type="checkbox" v-model="isFireFighter" class="checkbox" />
                </label>
            </div>

            <div></div>

            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Fire Fighter Rank</span>
                </div>
                <select v-model="staff.fireFighterRank" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Rank</option>
                    <option v-for="(rank, index) in choices.FireFighterRank" :key="index">
                        {{ rank }}
                    </option>
                </select>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Fire Fighter Role</span>
                </div>
                <select v-model="staff.fireFighterRole" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Role</option>
                    <option v-for="(role, index) in choices.FireFighterRole" :key="index">
                        {{ role }}
                    </option>
                </select>
            </label>
            <button class="btn btn-primary w-full col-span-2 pb-0.5 text-xl ">Submit</button>
        </form>
        
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/api.js'
import { useRouter } from 'vue-router'

const router = useRouter()

const choices = ref({
    gender: [],
    shift: [],
    FireFighterRole: [],
    FireFighterRank: [],
    station: []
});

const placeholderDate = new Date('11-22-2000')

const staff = ref( {
    name: 'John Doe',
    dob: placeholderDate,
    gender: 'Male',
    position: 'FireFighter',
    station: 'Main Fire Station',
    shift: [        
        'Mon 09:00 - 16:00',
        'Wed 09:00 - 16:00',
        'Thu 09:00 - 16:00',
    ],
    fire_fighter_rank: null,
    fire_fighter_role: null,
})

const isFireFighter = ref(false); // Will be set on fetch data

const fetchAvailableChoice = async () => {
    /**
    const response = await apiClient.get(`/staff/choice`)
    */

    // These are Place holder please write an API for it
    choices.value.gender = [
        'Male',
        'Female',
        'Other'
    ];

    choices.value.shift = [
        'Mon 09:00 - 16:00',
        'Tue 09:00 - 16:00',
        'Wed 09:00 - 16:00',
        'Thu 09:00 - 16:00',
        'Sat 09:00 - 16:00',
        'Sun 09:00 - 16:00',
    ];

    choices.value.FireFighterRole = [
        "Incident Commander",
        "Company Officer",
        "Hoseline Operator",
        "Nozzle Operator",
        "Vent Technician",
        "Search and Rescue Technician",
        "Medical Technician",
    ];

    choices.value.FireFighterRank = [
        "FireFighter",
        "Engineer",
        "Lieutenant",
        "Captain",
        "District Chief",
        "Division Chief",
        "Deputy Fire Chief",
        "Fire Chief",
    ];

    choices.value.station = [
        'Main Fire Station',
        'Downtown Fire Station',
        'Northside Fire Station',
    ];
}

const submitData = () => {
    const form = document.querySelector('form');
    if (!form.checkValidity()) form.reportValidity
    try {
        apiClient.post(`/staff/`, staff)
    } catch (error) {
        console.error('Submission failed:', error);
    }
    
    console.log(staff)
    router.push('/staff/')
}

onMounted(() => {
    fetchAvailableChoice();
});
</script>