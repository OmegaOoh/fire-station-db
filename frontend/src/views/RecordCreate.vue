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

            <div class="form-control w-full">
                <label>Reported Time</label>
                <input 
                    type="datetime-local" 
                    v-model="dispatch.reported_time" 
                    class="input input-bordered w-full mb-2" 
                />
            </div>

            <div class="form-control w-full">
                <label>Notified Time</label>
                <input 
                    type="datetime-local" 
                    v-model="dispatch.notified_time" 
                    class="input input-bordered w-full mb-2" 
                />
            </div>

            <div class="form-control w-full">
                <label>Resolve Time</label>
                <input 
                    type="datetime-local" 
                    v-model="dispatch.resolved_time" 
                    class="input input-bordered w-full mb-2" 
                />  
            </div>

            <div class="mb-4">
                <label class="label">
                    <span class="label-text">Station</span>
                </label>
                <select v-model="selectedStation" class="select select-bordered w-full" required>
                    <option disabled value="">Select a station</option>
                    <option v-for="(station, index) in stations" :key="index" :value="station">
                        {{ station.station_name }}
                    </option>
                </select>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 max-h-[75vh]">
                <div class="mb-4">
                    <label class="label">
                        <span class="label-text">Fire Engines</span>
                    </label>
                    <div class="p-2 rounded-lg max-h-[75vh] overflow-y-auto">
                        <div v-for="engine in selectedStation.fire_engine" :key="engine.id" class="flex items-center mb-2">
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
                        <div v-for="equipment in avaiquipment" :key="equipment.id" class="flex items-center mb-2">
                            <input class="checkbox" type="checkbox" :id="'equipment-' + equipment.id" v-model="equipment.selected" />
                            <label :for="'equipment-' + equipment.id" class="ml-2">{{ equipment.item_name }}</label>
                        </div>
                    </div>
                </div>

                <div class="mb-4">
                    <label class="label">
                        <span class="label-text">Fire Fighters</span>
                    </label>
                    <div class="p-2 rounded-lg max-h-[75vh] overflow-y-auto">
                        <div v-for="fighter in selectedStation.staff" :key="fighter.id" class="flex items-center mb-2">
                            <input v-if="fighter.is_fire_fighter" type="checkbox" class="checkbox" :id="'fighter-' + fighter.id" v-model="fighter.selected" />
                            <label v-if="fighter.is_fire_fighter" :for="'fighter-' + fighter.id" class="ml-2">{{ fighter.full_name }}</label>
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
import { ref, computed } from 'vue';
import { onMounted } from 'vue'

// const date = new Date()
const dispatch = ref({
    incident: '',
    address: '',
    station: '',
    reported_time: '',
    notified_time: '',
    resolved_time: '',
    fire_engine: [],
    equipment_used: [],
    fire_fighter: [],
});

const selectedStation = ref({
        staff: [],
        fire_engine: []
    })
const incidentTypes = ref([])
const stations = ref([])

const getAvailableTool = () => {
    const avaiFireEngine = selectedStation.value.fire_engine.filter(engine => engine.selected)
    const avaitool = []
    for (let engine of avaiFireEngine) {
        for (let equip of engine.equipment_detail) {
            equip.selected = false
            avaitool.push(equip)
        }
    }
    return avaitool;
}

const avaiquipment = computed(getAvailableTool);

const submitDispatch = () => {

    console.log(selectedStation.value)
    dispatch.value.fire_fighter = selectedStation.value.staff.filter(fighter => fighter.selected).map(fighter => fighter.firefighter_detail.id);

    const selectedEn = []
    for (let engine of selectedStation.value.fire_engine) {
        if (engine.selected) {
            selectedEn.push(engine.id)
        }
    }
    dispatch.value.station = selectedStation.value.id
    dispatch.value.fire_engine = selectedEn
    dispatch.value.equipment_used = avaiquipment.value.filter(equip => equip.selected).map(equip => equip.id)
    console.log(dispatch.value)
    apiClient.post(`/fire-station/dispatch/`, dispatch.value)
};

const fetchdata = async () => {
    const choice_res = await apiClient.get(`/fire-station/choice/`)
    incidentTypes.value = choice_res.data.incident_type

    const station_res = await apiClient.get(`/fire-station/`)
    stations.value = station_res.data
}

onMounted(() => {
    fetchdata()
})
</script>