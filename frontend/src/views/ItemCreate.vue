<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">{{station.station_name}}: Equipment and Fire Engines Management</h1>

        <!-- Equipment Section -->
        <div class="mb-8 max-h-[50vh]">
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
                <ul class="list-disc pl-5 grid grid-cols-2">
                    <li v-for="equipment in equipments" :key="equipment.id" class="mt-2 grid grid-cols-2">
                        {{ equipment.item_name }} ({{ formatDate(equipment.issue_date) }})
                        <button @click="removeEquipment(equipment.id)" class="btn btn-error btn-sm w-fit">Remove</button>
                    </li>
                </ul>
            </div>
        </div>

        <!-- Fire Engines Section -->
        <div class="max-h-[50vh]">
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
                    {{ equipment.item_name }} ({{ formatDate(equipment.date) }})
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
                                <li v-for="equipment in engine.equipments" :key="equipment.id" class="grid grid-cols-2 mt-2">
                                    {{ equipment.item_name }} ({{ formatDate(equipment.date) }})
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

// Sample placeholder data for equipment
const sampleEquipments = [
    { id: 1, item_name: "Fire Hose", date: "2022-01-15" },
    { id: 2, item_name: "Axe", date: "2022-02-20" },
    { id: 3, item_name: "Fire Extinguisher", date: "2022-03-10" },
    { id: 4, item_name: "Ladder", date: "2022-04-05" },
];

// Sample placeholder data for fire engines
const sampleFireEngines = [
    {
        id: 1, 
        engine_number: "101", 
        model: "Ford F-550", 
        license_plate: "ABC-1234", 
        equipments: [sampleEquipments[0], sampleEquipments[1]]
    },
    {
        id: 2, 
        engine_number: "102", 
        model: "Chevrolet Silverado", 
        license_plate: "XYZ-5678", 
        equipments: [sampleEquipments[2], sampleEquipments[3]]
    }
];

const addEquipment = () => {
    if (newEquipmentName.value && newEquipmentDate.value) {
        const newEquipment = {
            id: equipments.value.length + 1, // Simulating ID
            item_name: newEquipmentName.value,
            date: newEquipmentDate.value
        };
        equipments.value.push(newEquipment);
        newEquipmentName.value = '';
        newEquipmentDate.value = '';
    }
};

const addFireEngine = () => {
    if (newEngineNumber.value && newEngineModel.value && newEngineLicensePlate.value) {
        const newFireEngine = {
            id: fireEngines.value.length + 1, // Simulating ID
            engine_number: newEngineNumber.value,
            model: newEngineModel.value,
            license_plate: newEngineLicensePlate.value,
            equipments: selectedEquipments.value.map(id => equipments.value.find(eq => eq.id === id))
        };
        fireEngines.value.push(newFireEngine);
        newEngineNumber.value = '';
        newEngineModel.value = '';
        newEngineLicensePlate.value = '';
        selectedEquipments.value = [];
    }
};

const removeEquipment = (id) => {
    equipments.value = equipments.value.filter(equipment => equipment.id !== id);
};

const removeEquipmentFromEngine = (equipmentId, engineId) => {
    const engine = fireEngines.value.find(engine => engine.id === engineId);
    if (engine) {
        engine.equipments = engine.equipments.filter(equipment => equipment.id !== equipmentId);
    }
};

const removeFireEngine = (id) => {
    fireEngines.value = fireEngines.value.filter(engine => engine.id !== id);
};

// Function to format date
const formatDate = (dateString) => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return new Date(dateString).toLocaleDateString(undefined, options);
};

const fetchData = async() => {
    const equipment_res = await apiClient.get(`/fire-station/equipments/`)
    equipments.value = equipment_res.data;

    // equipments.value = sampleEquipments
    fireEngines.value = sampleFireEngines;
}

onMounted(() => {
    fetchData();
});
</script>