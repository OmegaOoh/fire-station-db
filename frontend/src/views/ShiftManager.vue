<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">Shift Manager</h1>

        <div class="mb-4">
            <input 
                type="text" 
                v-model="search" 
                placeholder="Search shifts..." 
                class="input input-bordered w-full mb-2" 
            />
        </div>

         <!-- Create Shift Form -->
         <form @submit.prevent="createShift" class="mb-4">
            <div class="flex space-x-4">
                <div>
                    <label for="day" class="block">Day of Week</label>
                    <select 
                        id="day" 
                        v-model="newShift.day" 
                        class="input input-bordered" 
                        required
                    >
                        <option disabled value="">Select a day</option>
                        <option v-for="day in days" :key="day" :value="day.value">{{ day.label }}</option>
                    </select>
                </div>
                <div>
                    <label for="startTime" class="block">Start Time</label>
                    <input 
                        type="time" 
                        id="startTime" 
                        v-model="newShift.shift_start" 
                        class="input input-bordered" 
                        required
                    />
                </div>
                <div>
                    <label for="endTime" class="block">End Time</label>
                    <input 
                        type="time" 
                        id="endTime" 
                        v-model="newShift.shift_end" 
                        class="input input-bordered" 
                        required
                    />
                </div>
                <div class="flex items-end">
                    <button type="submit" class="btn btn-primary">Create Shift</button>
                </div>
            </div>
        </form>

        <table class="table w-full">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Day of Week</th>
                    <th>Start Time</th>
                    <th>End Time</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="shift in shifts" :key="shift.id">
                    <td>{{ shift.id }}</td>
                    <td>{{ shift.day }}</td>
                    <td>{{ formatTime(shift.shift_start) }}</td>
                    <td>{{ formatTime(shift.shift_end) }}</td>
                    <td>
                        <button v-if="shift.removeable" @click="removeShift(shift.id)" class="btn btn-danger btn-sm">Remove</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import apiClient from '@/api';
import { ref, onMounted } from 'vue';

const shifts = ref([]);

const search = ref('');
const newShift = ref({
    day: '',
    shift_start: '',
    shift_end: ''
});
const days = ref([])

const formatTime = (time) => {
    const [hour, minute] = time.split(':');
    const formattedHour = hour % 12 || 12; // Convert to 12-hour format
    const period = hour < 12 ? 'AM' : 'PM';
    return `${formattedHour}:${minute} ${period}`;
};

const createShift = async () => {
    await apiClient.post(`/fire-station/shift/`, newShift.value)
    fetchdata()
    // Reset the form
    newShift.value.day = '';
    newShift.value.start_time = '';
    newShift.value.end_time = '';
};

const removeShift = async (id) => {
    await apiClient.delete(`/fire-station/shift/${id}/`)
    fetchdata()
};

const fetchdata = async () => {
    const shift_res = await apiClient.get(`/fire-station/shift/`)
    shifts.value = shift_res.data
}

const fetchChoice = async () => {
    const choice_res = await apiClient.get(`/fire-station/choice/`)
    days.value = choice_res.data.day_of_week
}

onMounted(
    () => {
        fetchChoice()
        fetchdata()
    }
)
</script>