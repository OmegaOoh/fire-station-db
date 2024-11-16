<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl">
            New Staff
        </h2>
        <form ref="staffForm" @submit.prevent="submitData" class="my-4 grid grid-col-1 md:grid-cols-2 gap-20 w-full">
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Full Name</span>
                </div>
                <input v-model="fullName" class="input input-bordered rounded-md ml-4 w-full" type="text" required>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Date of Birth</span>
                </div>
                <input v-model="dob" class="input input-bordered rounded-md ml-4 w-full" type="date" required>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Gender</span>
                </div>
                <select v-model="gender" class="select select-bordered ml-4 w-full">
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
                <input v-model="position" class="input input-bordered rounded-md ml-4 w-full" type="text" required>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Station</span>
                </div>
                <select v-model="station" class="select select-bordered ml-4 w-full" required>
                    <option disabled selected>Station</option>
                    <option v-for="(station, index) in choices.station" :key="index">
                        {{ station }}
                    </option>
                </select>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Shift</span>
                </div>
                <select v-model="shift" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Shift</option>
                    <option v-for="(shift, index) in choices.shift" :key="index">
                        {{ shift }}
                    </option>
                </select>
            </label>

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
                <select v-model="fireFighterRank" class="select select-bordered ml-4 w-full">
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
                <select v-model="fireFighterRole" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Role</option>
                    <option v-for="(role, index) in choices.FireFighterRole" :key="index">
                        {{ role }}
                    </option>
                </select>
            </label>
            <button class="btn btn-primary w-full">Submit</button>
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

const fullName = ref('');
const dob = ref(null);
const gender = ref(null);
const station = ref(null);
const shift = ref(null);
const position = ref('');
const isFireFighter = ref(false);
const fireFighterRank = ref('');
const fireFighterRole = ref('');

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
        'Station A',
        'Station B',
        'Station C',
    ];
}

const submitData = () => {
    const form = document.querySelector('form');
    if (!form.checkValidity()) form.reportValidity
    let data = {
        name: fullName.value,
        dob: dob.value,
        gender: gender.value,
        position: position.value,
        station: station.value,
        shift: shift.value,
    }
    if (isFireFighter.value) {
        const extended = {
            fire_fighter_role: fireFighterRole.value,
            fire_fighter_rank: fireFighterRank.value
        }
        data = { ...data, ...extended }
    }
    try {
        apiClient.post(`/staff/`, data)
    } catch (error) {
        console.error('Submission failed:', error);
    }
    
    console.log(data)
    router.push('/staff/')
}

onMounted(() => {
    fetchAvailableChoice();
});
</script>