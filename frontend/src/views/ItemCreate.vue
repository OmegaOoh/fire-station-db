<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">{{station.station_name}}: Equipment and Fire Engines Management</h1>

        <!-- Equipment Section -->
        <div class="mb-8">
            <h2 class="text-2xl font-semibold mb-4">Equipment</h2>
            <input 
                type="text" 
                v-model="newEquipmentName" 
                placeholder="Enter equipment name..." 
                class="input input-bordered w-full mb-2" 
            />
            <input 
                type="date" 
                v-model="newEquipmentDate" 
                class="input input-bordered w-full mb-2" 
            />
            <button @click="addEquipment" class="btn btn-primary">Add Equipment</button>

            <div class="mt-4">
                <h3 class="text-xl font-semibold">Equipment List</h3>
                <ul class="list-disc pl-5 grid grid-cols-2 max-h-[25vh] overflow-y-auto">
                    <li v-for="equipment in equipments" :key="equipment.id" class="mt-2 grid grid-cols-2">
                        {{ equipment.item_name }} ({{ formatDate(equipment.issue_date) }})
                        <button @click="removeEquipment(equipment.id)" class="btn btn-error btn-sm w-fit">Remove</button>
                    </li>
                </ul>
            </div>
        </div>

        <!-- Fire Engines Section -->
        <div>
            <h2 class="text-2xl font-semibold mb-4">Fire Engines</h2>
            <input 
                type="number" 
                v-model="newEngineNumber" 
                placeholder="Engine Number" 
                class="input input-bordered w-full mb-2" 
            />
            <input 
                type="text" 
                v-model="newEngineModel" 
                placeholder="Model" 
                class="input input-bordered w-full mb-2" 
            />
            <input 
                type="text" 
                v-model="newEngineLicensePlate" 
                placeholder="License Plate" 
                class="input input-bordered w-full mb-2" 
            />
            <div class="font-semibold mb-1">Equipments</div>
            <select v-model="selectedEquipments" multiple class="select select-bordered w-full mb-2">
                <option v-for="equipment in equipments" :key="equipment.id" :value="equipment.id">
                    {{ equipment.item_name }} ({{ formatDate(equipment.issue_date) }})
                </option>
            </select>
            <button @click="addFireEngine" class="btn btn-primary">Add Fire Engine</button>

            <div class="mt-4">
                <h3 class="text-xl font-semibold">Fire Engines List</h3>
                <template v-for="engine in fireEngines" :key="engine.id">
                    <div class="collapse collapse-arrow bg-base-300 mb-4">
                        <input type="radio" name="my-accordion-2" checked="checked"/>
                        <div class="collapse-title text-xl font-bold">
                            {{ engine.model }} (Engine No: {{ engine.engine_number }}, License Plate: {{ engine.license_plate }})
                        </div>

                        <div class="collapse-content">
                            <p class="Equipments:"></p>
                            <ul class="pl-5 list-disc">
                                <li v-for="equipment in engine.equipment_detail" :key="equipment.id" class="grid grid-cols-2 mt-2">
                                    {{ equipment.item_name }} ({{ formatDate(equipment.issue_date) }})
                                    <button @click="removeEquipmentFromEngine(equipment.id, engine.id)" class="btn btn-error btn-sm w-fit">Remove</button>
                                </li>
                            </ul>
                            <button @click="removeFireEngine(engine.id)" class="btn btn-error btn-sm">Remove Fire Engine</button>
                        </div>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>

<script setup>
import apiClient from '@/api';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const station = ref({
    station_name: 'Main Fire Station',
    address: '123 Main St, Springfield',
    staff_capacity: 20,
    fire_engine_capacity: 5
});
const equipments = ref([]);
const fireEngines = ref([]);

const newEquipmentName = ref('');
const newEquipmentDate = ref('');
const newEngineNumber = ref('');
const newEngineModel = ref('');
const newEngineLicensePlate = ref('');
const selectedEquipments = ref([]);

const addEquipment = async () => {
    const data = {
        item_name: newEquipmentName.value,
        issue_date: newEquipmentDate.value
    }

    if (!(newEquipmentName.value && newEquipmentDate.value)){
        return
    }

    const res = await apiClient.post(`fire-station/equipments/`, data)
    equipments.value = res.data
};

const addFireEngine = async () => {
    if (newEngineNumber.value && newEngineModel.value && newEngineLicensePlate.value) {
        const newFireEngine = {
            station: route.params.id,
            engine_number: newEngineNumber.value,
            model: newEngineModel.value,
            license_plate: newEngineLicensePlate.value,
            equipments: selectedEquipments.value
        };

        await apiClient.post(`/fire-station/fire-engine/`, newFireEngine)
        fetchData()

        newEngineNumber.value = '';
        newEngineModel.value = '';
        newEngineLicensePlate.value = '';
        selectedEquipments.value = [];
    }
};

const removeEquipment = async (id) => {
    const res = await apiClient.delete(`fire-station/equipments/?equipments_to_remove=${id}`)
    equipments.value = res.data
};

const removeEquipmentFromEngine = async (equipmentId, engineId) => {
    const engine = fireEngines.value.find(engine => engine.id === engineId);
    
    if (engine) {
        const removedEquipment = engine.equipments.filter(equip_id => equip_id != equipmentId);
        const data = {
            id: engine.id,
            equipments: removedEquipment
        }
        await apiClient.put(`/fire-station/fire-engine/`, data)
        fetchData()
    }
};

const removeFireEngine = async(id) => {
    await apiClient.delete(`/fire-station/fire-engine/?id=${id}`)
    fetchData()
};

// Function to format date
const formatDate = (dateString) => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return new Date(dateString).toLocaleDateString(undefined, options);
};

const fetchData = async() => {

    

    const equipment_res = await apiClient.get(`/fire-station/equipments/`)
    equipments.value = equipment_res.data;

    const station_res = await apiClient.get(`/fire-station/${route.params.id}`)
    station.value = station_res.data
    fireEngines.value = station_res.data.fire_engine;
}

onMounted(() => {
    fetchData();
});
</script>