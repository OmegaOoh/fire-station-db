<template>
    <div class="pt-4 px-4">
        <h2 class="font-bold text-4xl pb-4">{{ station.station_name }}</h2>
        <!--Overall Data-->
        <div class="grid grid-cols-2 ml-4 text-xl">
            <p class="col-span-2"><strong>Address:</strong> {{ station.address }}</p>
            <p><strong>Staff Capacity:</strong> {{ station.staff_capacity }}</p>
            <p><strong>Fire Engine Capacity:</strong> {{ station.fire_engine_capacity }}</p>
            <p class="font-bold text-2xl">Firefighter on each Role</p>
            <div class="stats bg-base-200 shadow w-full">
                <div class="stat place-items-center" v-for="(data, index) in rollCount" :key="index">
                    <div class="stat-title">{{ data.firefighter__role }}</div>
                    <div class="stat-value" :class="colorByIndex(index)">{{ data.amount }}</div>
                </div>
            </div>
            <p class="font-bold text-2xl">Firefighter on each Rank</p>
            <div class="stats bg-base-200 shadow w-full">
                <div class="stat place-items-center" v-for="(data, index) in rankCount" :key="firefighter__rank">
                    <div class="stat-title">{{ getRankName(data.firefighter__rank) }}</div>
                    <div class="stat-value" :class="colorByIndex(index)">{{ data.amount }}</div>
                </div>
            </div>
        </div>
        <!--Staff and Equipments-->
        <div>
            <h3 class="text-2xl mt-4 font-bold mb-2">Staff</h3>
            <template v-if="staff.length">
                <template v-for="staffData in staff" :key="staffData.id">
                    <div class="collapse collapse-arrow bg-base-300 mb-4">
                        <input type="radio" name="my-accordion-2" checked="checked" />
                        <div class="collapse-title text-xl font-medium">{{ staffData.full_name }}
                            <div class="badge badge-secondary" v-if="staffData.is_fire_fighter">Fire Fighter</div>
                        </div>
                            <div class="collapse-content grid grid-cols-1 md:grid-cols-2">
                                <p><strong>Date of Birth:</strong> {{ staffData.dob }}</p>
                                <p><strong>Gender:</strong> {{ staffData.gender }}</p>
                                <p><strong>Position:</strong> {{ staffData.position }}</p>
                                <p v-if="staffData.fire_fighter_rank"><strong>Fire Fighter Rank:</strong> {{ staffData.fire_fighter_rank }}</p>
                                <p v-if="staffData.fire_fighter_role"><strong>Fire Fighter Role:</strong> {{ staffData.fire_fighter_role }}</p>
                                <strong class="col-span-2">
                                    Shifts:
                                </strong>
                                <ul class="col-span-2 grid grid-cols-1 md:grid-cols-6 ml-2">
                                    <li v-for="(shift, index) in staffData.shift" :key="index">
                                        {{ shift.day }} {{ shift.shift_start }} - {{ shift.shift_end }}
                                    </li>
                                </ul>
                            </div>
                    </div>
                </template>
            </template>

            <template v-else>
                <p>No staff available for this station.</p>
            </template>
        </div>

        <div>
            <div class="flex flex-row">
                <h3 class="text-2xl font-bold mt-4 mb-2 mr-3">Fire Engines</h3> 
                <router-link class="btn btn-primary" :to="`/station/${station.id}/manage`"> Manage </router-link>
            </div>
            <template v-if="fireEngines.length">

                <template v-for="engine in fireEngines" :key="engine.id">
                    <div class="collapse collapse-arrow bg-base-300 mb-4">
                        <input type="radio" name="my-accordion-2" checked="checked" />
                        <div class="collapse-title text-xl font-medium">{{ engine.engine_number }}
                        </div>
                            <div class="collapse-content grid grid-cols-1 md:grid-cols-2">
                                <p><strong>Model:</strong> {{ engine.model }}</p>
                                <p><strong>License Plate:</strong> {{ engine.license_plate }}</p>
                                <strong>Equipments:</strong>
                                <ul class="col-span-2 grid grid-cols-1 md:grid-cols-6 ml-2">
                                    <li v-for="(equipment, index) in engine.equipment_detail" :key="index">
                                        {{ equipment.item_name }} ({{ equipment.issue_date }})
                                    </li>
                                </ul>
                            
                            </div>
                        </div>
                </template>
            </template>
            <template v-else>
                <p>No fire engines available for this station.</p>
            </template>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { onMounted} from 'vue'
import { useRoute } from 'vue-router';
import apiClient from '@/api.js';

const route = useRoute();
const station = ref({});
const staff = ref([]);
const fireEngines = ref([]);
const rollCount = ref([]);
const rankCount = ref([]);
const rankList = ref([]);

const fetchStationDetails = async () => {
    const stationId = route.params.id;
    try {
        const response = await apiClient.get(`/fire-station/${stationId}/`);
        station.value = response.data;
        fireEngines.value = response.data.fire_engine
        staff.value = response.data.staff;
        rollCount.value = response.data.role_count	
        rankCount.value = response.data.rank_count
        console.log(rollCount.value)
    } catch (error) {
        console.error('Error fetching station details:', error);
    }
    const choice_res = await apiClient.get(`/fire-station/choice/`)
    rankList.value = choice_res.data.fire_fighter_rank
    console.log(rankList.value)
};

const getRankName = (rankId) => {
    const filtered = rankList.value.filter(rank => rank.value == rankId)
    if (filtered.length > 0) {
        return filtered[0].label
    } else {
        return "-"
    }
}

onMounted(() => {
    fetchStationDetails()
})

const colorByIndex = (index) => {
    return index % 2 === 0 ? 'text-neutral-content' : 'text-primary';
}

</script>