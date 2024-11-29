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
                <input v-model="staff.full_name" class="input input-bordered rounded-md ml-4 w-full" type="text" required>
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
                    <option v-for="(gender, index) in choices.gender" :key="index" :value="gender.value">
                        {{ gender.label }}
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
                        <input type="checkbox" :id="'shift-' + index" v-model="staff.shift" :value="shift.id" class="checkbox" />
                        <label :for="'shift-' + index" class="ml-2">{{ shift.day }} {{ shift.shift_start.slice(0, 5) }} - {{ shift.shift_end.slice(0, 5) }}</label>
                    </div>
                </div>
            </div>
            <div v-if="staff.is_fire_fighter" class="my-4 grid grid-col-1 md:grid-cols-2 gap-20 w-full col-span-2">
                <label class="form-control w-full">
                    <div class="label">
                        <span class="label-text text-xl">Fire Fighter Rank</span>
                    </div>
                    <select v-model="staff.fireFighterRank" class="select select-bordered ml-4 w-full">
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
                    <select v-model="staff.fireFighterRole" class="select select-bordered ml-4 w-full">
                        <option disabled selected>Role</option>
                        <option v-for="(role, index) in choices.FireFighterRole" :key="index" :value="role.value">
                            {{ role.label }}
                        </option>
                    </select>
                </label>
                <button class="btn btn-primary w-full col-span-2 pb-0.5 text-xl ">Submit</button>
            </div>
        </form>
        
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/api.js'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()
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
    full_name: 'John Doe',
    dob: placeholderDate,
    gender: '',
    position: '',
    station: '',
    shift: [],
    is_fire_fighter: false
})

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

    const staff_res = await apiClient.get(`/fire-station/staff/${route.params.id}/`)
    staff.value.name = staff_res.data.full_name
    staff.value.dob = new Date(staff_res.data.dob)
    staff.value.gender = staff_res.data.gender
    staff.value.position = staff_res.data.position
    staff.value.is_fire_fighter = staff_res.data.is_fire_fighter

}

const submitData = () => {
    const form = document.querySelector('form');
    console.log(staff.value.shift)
    console.log("shift")

    if (!form.checkValidity()) form.reportValidity

    try {
        apiClient.put(`/fire-station/staff/${route.params.id}/`, staff.value)
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