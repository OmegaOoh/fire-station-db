<template>
    <div class="pt-4 px-4">
        <h1 class="font-extrabold text-5xl">Stats</h1>
        <!-- Filters -->
        <div class="flex space-x-4 my-4">
            <select v-model="selectedStation" class="select w-full max-w-xs">
                <option value="">All Stations</option>
                <option v-for="station in stations" :key="station" :value="station">{{ station }}</option>
            </select>

            <select v-model="selectedMonth" class="select w-full max-w-xs">
                <option value="">All Months</option>
                <option v-for="month in months" :key="month" :value="month">{{ month }}</option>
            </select>

            <select v-model="selectedIncidentType" class="select w-full max-w-xs">
                <option value="">All Incident Types</option>
                <option v-for="type in incidentTypes" :key="type" :value="type">{{ type }}</option>
            </select>
            <button class="btn btn-neutral " @click="filterData">Search</button>
        </div>
        <div class="flex w-full flex-col my-6">
            <div class="stats bg-base-200 shadow w-full mb-4">
                <div class="stat place-items-center">
                    <div class="stat-title">Dispatch Response</div>
                    <div class="stat-value">{{ responseData.responded }}</div>
                    <div class="stat-desc text-secondary font-semibold text-lg"></div>
                </div>

                <div class="stat place-items-center">
                    <div class="stat-title">Most Incident Type</div>
                    <div class="stat-value">{{ responseData.most_type }}</div>
                    <div class="stat-desc text-secondary font-semibold text-lg">{{ responseData.most_percentage }} % of Dispatch</div>
                </div>

                <div class="stat place-items-center">
                    <div class="stat-title">Average Time Resolved</div>
                    <div class="stat-value">{{ responseData.avg_time_resolved }} mins</div>
                </div>

                <div class="stat place-items-center">
                    <div class="stat-title">Fire Fighter on Duty</div>
                    <div class="stat-value">{{ responseData.active_duty }}</div>
                    <div class="stat-desc text-secondary font-semibold text-lg">across {{ responseData.stations_num }} stations</div>
                </div>
            </div>
        </div>
        <div class="stats bg-base-200 shadow w-full mb-8">
            <div class="stat place-items-center" v-for="(data, index) in responseData.by_month" :key="data.month">
                <div class="stat-title">{{ data.month }}</div>
                <div class="stat-value" :class="colorByIndex(index)">{{ data.dispatch }}</div>
                <div class="stat-desc">Dispatched</div>
            </div>
        </div>
        <div class="stats bg-base-200 shadow w-full">
            <div class="stat place-items-center" v-for="(data, index) in responseData.by_station" :key="data.station">
                <div class="stat-title">{{ data.station }}</div>
                <div class="stat-value" :class="colorByIndex(index)">{{ data.dispatch }}</div>
                <div class="stat-desc">Dispatched</div>
            </div>
        </div>
    </div>
    <div>
        
    </div>
</template>

<script setup>
import { ref } from 'vue';

const responseData = ref({
    responded: 200,
    most_type: "Structure Fire",
    most_percentage: 70,
    stations_num: 1,
    active_duty: 8,
    avg_time_resolved: 25,
    by_station: [ 
        {station: 'Main Station', dispatch: 200} // All if no filter
    ],
    by_month: [ // Alter this on filter
        { month: 'Jan', dispatch: 230 },
        { month: 'Feb', dispatch: 120 },
        { month: 'Mar', dispatch: 100 },
        { month: 'Apr', dispatch: 120 },
        { month: 'May', dispatch: 200 },
        { month: 'Jun', dispatch: 300 },
        { month: 'Jul', dispatch: 123 },
        { month: 'Aug', dispatch: 200 },
        { month: 'Sep', dispatch: 90 },
        { month: 'Oct', dispatch: 84 },
        { month: 'Nov', dispatch: 242 },
        { month: 'Dec', dispatch: 431 },
    ]
})

// Filter state
const selectedStation = ref('');
const selectedMonth = ref('');
const selectedIncidentType = ref('');

// Example data for filtering
const stations = ['Station 1', 'Station 2', 'Station 3', 'Station 4', 'Station 5']; // TODO Fetch Available choice from backend
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const incidentTypes = ['Vehicle Fire', 'Structure Fire', 'Medical Emergency ', 'Hazardous Materials', 'Rescue']; // TODO Fetch Available choice from backend

const filterData = async() => {
    const filterParam = {};

    if (selectedStation.value) {
        filterParam['station'] = selectedStation.value
    }
    if (selectedMonth.value) {
        filterParam['month'] = selectedMonth.value
    }
    if (selectedIncidentType.value) {
        filterParam['incident'] = selectedIncidentType.value
    }

    // const response = apiClient.get(apiPath, {params: filterParam})
    // filteredData = response.data
    console.log(filterParam);
};

const colorByIndex = (index) => {
    return index % 2 === 0 ? '' : 'text-primary';
}
</script>