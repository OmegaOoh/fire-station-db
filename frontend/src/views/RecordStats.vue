<template>
    <div class="pt-4 px-4">
        <h1 class="font-extrabold text-5xl">Stats</h1>
        <!-- Filters -->
        <div class="flex space-x-4 my-4">
            <select v-model="selectedStation" class="select w-full max-w-xs">
                <option value="">All Stations</option>
                <option v-for="station in stations" :key="station" :value="station.id">{{ station.station_name }}</option>
            </select>

            <select v-model="selectedMonth" class="select w-full max-w-xs">
                <option value="">All Months</option>
                <option v-for="month in months" :key="month" :value="month.val">{{ month.month }}</option>
            </select>

            <select v-model="selectedIncidentType" class="select w-full max-w-xs">
                <option value="">All Incident Types</option>
                <option v-for="type in incidentTypes" :key="type" :value="type.value">{{ type.label }}</option>
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
            <div class="stat place-items-center" v-for="(data, index) in months" :key="data.month">
                <div class="stat-title">{{ data.month }}</div>
                <div class="stat-value" :class="colorByIndex(index)">{{ getMonthData(data.val) }}</div>
                <div class="stat-desc">Dispatched</div>
            </div>
        </div>
        <div class="stats bg-base-200 shadow w-full">
            <div class="stat place-items-center" v-for="(data, index) in responseData.by_station" :key="data.station">
                <div class="stat-title">{{ data.station__station_name }}</div>
                <div class="stat-value" :class="colorByIndex(index)">{{ data.number_of_dispatches }} <span class="stat-desc text-lg">Dispatched</span></div>
                <div class="stat-desc text-sm font-semibold" :class="colorByIndex(index + 1)"> Avg. {{ data.average_time_resolved / 60 }} Minutes</div>
            </div>
        </div>
    </div>
    <div>
        
    </div>
</template>

<script setup>
import apiClient from '@/api';
import { ref, onMounted } from 'vue';

const responseData = ref({
    responded: 200,
    most_type: "Structure Fire",
    most_percentage: 70,
    stations_num: 1,
    active_duty: 8,
    avg_time_resolved: 25,
    by_station: [],
    by_month: [],
    by_incident: []
})

// Filter state
const selectedStation = ref('');
const selectedMonth = ref('');
const selectedIncidentType = ref('');

// Example data for filtering
const stations = ref([]);
const incidentTypes = ref([]);
const months = [
    {month: 'Jan', val: 1}, 
    {month: 'Feb', val: 2}, 
    {month: 'Mar', val: 3}, 
    {month: 'Apr', val: 4}, 
    {month: 'May', val: 5}, 
    {month: 'Jun', val: 6}, 
    {month: 'Jul', val: 7}, 
    {month: 'Aug', val: 8}, 
    {month: 'Sep', val: 9}, 
    {month: 'Oct', val: 10}, 
    {month: 'Nov', val: 11}, 
    {month: 'Dec', val: 12}
];

const filterData = async() => {
    let filterParam = "";

    if (selectedStation.value) {
        filterParam += "station=" + selectedStation.value + "&"
    }
    if (selectedMonth.value) {
        filterParam += "months=" + selectedMonth.value + "&"
    }
    if (selectedIncidentType.value) {
        filterParam += "incident=" + selectedIncidentType.value + "&"
    }
    fetchData(filterParam)
};

const colorByIndex = (index) => {
    return index % 2 === 0 ? 'text-neutral-content' : 'text-primary';
}

const fetchChoices = async () => {
    const station_res = await apiClient.get(`/fire-station/`)
    stations.value = station_res.data 

    const choice_res = await apiClient.get(`/fire-station/choice/`)
    months.value = choice_res.data.month
    incidentTypes.value = choice_res.data.incident_type
}

const fetchData = async (filter="") => {
    const by_station_res = await apiClient.get(`/fire-station/dispatch-aggregate/?group_by=station__station_name` + "&" + filter)
    responseData.value.by_station = by_station_res.data 

    const by_month_res = await apiClient.get(`/fire-station/dispatch-aggregate/?group_by=reported_time__month` + "&" + filter)
    responseData.value.by_month = by_month_res.data 

    const by_in_res = await apiClient.get(`/fire-station/dispatch-aggregate/?group_by=incident` + "&" + filter)
    if (by_in_res.data.length > 0){
        responseData.value.most_type = getIncidentName(by_in_res.data[0].incident)
        responseData.value.most_percentage = by_in_res.data[0].dispatch_percentage
    } else {
        responseData.value.most_type = "-"
        responseData.value.most_percentage = 0
    }

    const total = await apiClient.get(`/fire-station/dispatch-aggregate/` + "?" + filter)
    responseData.value.responded = total.data.number_of_dispatches
    responseData.value.avg_time_resolved = total.data.average_time_resolved / 60
}

const getMonthData = (month_id) => {
    const data = responseData.value.by_month.filter(month => month.reported_time__month == month_id)
    if (data.length != 0) { return data[0].number_of_dispatches } else {return 0}
}

const getIncidentName = (in_id) => {
    const data = incidentTypes.value.filter(incident => incident.value == in_id)
    if (data.length != 0) { return data[0].label } else {return ""}
}


onMounted(
    () => {
        fetchData()
        fetchChoices()
    }
)
</script>