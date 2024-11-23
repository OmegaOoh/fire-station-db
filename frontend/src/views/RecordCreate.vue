<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">Create Dispatch</h1>
        <form @submit.prevent="submitDispatch">
            <div class="mb-4">
                <label class="label">
                    <span class="label-text">Incident Type</span>
                </label>
                <select v-model="dispatch.incident" class="select select-bordered w-full" required>
                    <option disabled value="">Select an incident type</option>
                    <option v-for="(incident, index) in incidentTypes" :key="index" :value="incident.value">
                        {{ incident.label }}
                    </option>
                </select>
            </div>

            <div class="mb-4">
                <label class="label">
                    <span class="label-text">Address</span>
                </label>
                <input type="text" v-model="dispatch.address" class="input input-bordered w-full" placeholder="Enter address" required />
            </div>

            <div class="mb-4">
                <label class="label">
                    <span class="label-text">Station</span>
                </label>
                <select v-model="dispatch.station" class="select select-bordered w-full" required>
                    <option disabled value="">Select a station</option>
                    <option v-for="(station, index) in stations" :key="index" :value="station.id">
                        {{ station.name }}
                    </option>
                </select>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 max-h-[75vh]">
                <div class="mb-4">
                    <label class="label">
                        <span class="label-text">Fire Engines</span>
                    </label>
                    <div class="p-2 rounded-lg max-h-[75vh] overflow-y-auto">
                        <div v-for="engine in fireEngines" :key="engine.id" class="flex items-center mb-2">
                            <input type="checkbox" class="checkbox" :id="'engine-' + engine.id" v-model="engine.selected" />
                            <label :for="'engine-' + engine.id" class="ml-2">{{ engine.engine_number }}</label>
                        </div>
                    </div>
                </div>

                <div class="mb-4">
                    <label class="label">
                        <span class="label-text">Equipment Used</span>
                    </label>
                    <div class="p-2 rounded-lg max-h-[75vh] overflow-y-auto">
                        <div v-for="equipment in equipmentList" :key="equipment.id" class="flex items-center mb-2">
                            <input class="checkbox" type="checkbox" :id="'equipment-' + equipment.id" v-model="equipment.selected" />
                            <label :for="'equipment-' + equipment.id" class="ml-2">{{ equipment.name }}</label>
                        </div>
                    </div>
                </div>

                <div class="mb-4">
                    <label class="label">
                        <span class="label-text">Fire Fighters</span>
                    </label>
                    <div class="p-2 rounded-lg max-h-[75vh] overflow-y-auto">
                        <div v-for="fighter in fireFighters" :key="fighter.id" class="flex items-center mb-2">
                            <input type="checkbox" class="checkbox" :id="'fighter-' + fighter.id" v-model="fighter.selected" />
                            <label :for="'fighter-' + fighter.id" class="ml-2">{{ fighter.name }}</label>
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-control mt-6">
                <button type="submit" class="btn btn-primary">Create Dispatch</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import apiClient from '@/api';
import { ref } from 'vue';

const dispatch = ref({
    incident: '',
    address: '',
    station: '',
    fireEngines: [],
    equipmentUsed: [],
    fireFighters: []
});
const incidentTypes = ref([])
const stations = ref([])


const choice_res = apiClient.get(`/fire-station/choices/`)
incidentTypes.value = choice_res.data.incident_type

const station_res = await apiClient.get(`/fire-station/`)
stations.value = station_res.data

const fireEngines = ref([
    { id: 1, engine_number: '103', selected: false },
    { id: 2, engine_number: '102', selected: false },
    { id: 3, engine_number: '306', selected: false }
]);

const equipmentList = ref([
    { id: 1, name: 'Hoses', selected: false },
    { id: 2, name: 'Ladders', selected: false },
    { id: 3, name: 'Fire Extinguishers', selected: false }
]);

const fireFighters = ref([
    { id: 1, name: 'John Doe', selected: false },
    { id: 2, name: 'Jane Smith', selected: false },
    { id: 3, name: 'Emily Johnson', selected: false },
    { id: 4, name: 'Harper Dope', selected: false },
    { id: 5, name: 'Abby Swan', selected: false },
    { id: 6, name: 'Top Ten', selected: false },
    { id: 7, name: 'Jame Samson', selected: false },
]);

const submitDispatch = () => {
    dispatch.value.fireEngines = fireEngines.value.filter(engine => engine.selected);
    dispatch.value.equipmentUsed = equipmentList.value.filter(equipment => equipment.selected);
    dispatch.value.fireFighters = fireFighters.value.filter(fighter => fighter.selected);
    console.log('Dispatch created:', dispatch.value);
};
</script>