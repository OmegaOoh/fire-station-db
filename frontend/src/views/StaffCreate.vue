<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl">New Staff</h2>
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
                    <option v-for="(gender, index) in choices.gender" :key="index" :value="gender.value">
                        {{ gender.label }}
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
                    <option v-for="(station, index) in choices.station" :key="index" :value="station.id">
                        {{ station.station_name }}
                    </option>
                </select>
            </label>

            <div class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Shifts</span>
                </div>
                <div class="ml-4 grid grid-cols-2">
                    <div v-for="(shift, index) in choices.shift" :key="index" class="flex items-center mb-2">
                        <input type="checkbox" :id="'shift-' + index" v-model="selectedShifts" :value="shift.id" class="checkbox" />
                        <label :for="'shift-' + index" class="ml-2">{{ shift.day }} {{ shift.shift_start.slice(0, 5) }} - {{ shift.shift_end.slice(0, 5) }}</label>
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
                <select v-model="fireFighterRank" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Rank</option>
                    <option v-for="(rank, index) in choices.FireFighterRank" :key="index" :value="rank.value">
                        {{ rank.label }}
                    </option>
                </select>
            </label>
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text text-xl">Fire Fighter Role</span>
                </div>
                <select v-model="fireFighterRole" class="select select-bordered ml-4 w-full">
                    <option disabled selected>Role</option>
                    <option v-for="(role, index) in choices.FireFighterRole" :key="index" :value="role.value">
                        {{ role.label }}
                    </option>
                </select>
            </label>
            <button class="btn btn-primary w-full col-span-2 pb-0.5 text-xl">Submit</button>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/api.js';
import { useRouter } from 'vue-router';

const router = useRouter();

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
const position = ref('');
const isFireFighter = ref(false);
const fireFighterRank = ref('');
const fireFighterRole = ref('');
const selectedShifts = ref([]);

const fetchAvailableChoice = async () => {

    // Fetch static choice
    const choice_res = await apiClient.get(`/fire-station/choice/`)
    choices.value.FireFighterRole = choice_res.data.fire_fighter_role
    choices.value.FireFighterRank = choice_res.data.fire_fighter_rank
    choices.value.gender = choice_res.data.gender
    const shift_res = await apiClient.get(`/fire-station/shift/`)
    choices.value.shift = shift_res.data

    const station_res = await apiClient.get(`/fire-station/`)
    choices.value.station = station_res.data
}

const submitData = async() => {
    const form = document.querySelector('form');
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }
    
    let data = {
        full_name: fullName.value,
        dob: dob.value,
        gender: gender.value,
        position: position.value,
        station: station.value,
        shift: selectedShifts.value,
    }    
    if (isFireFighter.value) {
        const firefighter = {
            role: fireFighterRole.value,
            rank: fireFighterRank.value
        }
        data.firefighter = firefighter
    }
    
    try {
        await apiClient.post(`/fire-station/staff/`, data);
        router.push('/staff/');
    } catch (error) {
        console.error('Submission failed:', error);
    }
    
}

onMounted(() => {
    fetchAvailableChoice();
});
</script>