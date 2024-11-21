<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">
            Record Stats
        </h1>
        <template v-if="!overallData.year_incident.years==[]">
            <h2 class="text-3xl font-bold mb-6">Overall Data</h2>
            <div class="stats stats-vertical lg:stats-horizontal shadow w-full">
                <div class="stat">
                    <div class="stat-title font-semibold"># of Response</div>
                    <div class="stat-value text-secondary">{{ overallData.incident_nums }}</div>
                    <div class="stat-desc">{{ firstYear }} - {{ lastYear }}</div>
                </div>

                <div class="stat">
                    <div class="stat-title font-semibold">Most Incident Type</div>
                    <div class="stat-value text-primary">{{ overallData.most_incident_type }}</div>
                </div>
            </div>
            <h2 class="text-3xl font-bold mb-6">Explore Data</h2>
            <div class="stats stats-vertical lg:stats-horizontal shadow w-full">
                <div class="stat">
                    <div class="stat-title font-semibold"># of Response</div>
                    <div class="stat-value text-secondary">{{ data.incident }}</div>
                    <div class="stat-desc">Jan 1st - Feb 1st</div>
                </div>

                <div class="stat">
                    <div class="stat-title font-semibold">Average Time Resolved</div>
                    <div class="stat-value text-primary">{{ data.avg_resolve }}</div>
                    <div class="stat-desc">Minutes</div>
                </div>
            </div>
        </template>
        <template v-else> 
            <h1 class='text-4xl text-primary font-semibold'>
                No Data
            </h1> 
        </template>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const overallData = ref({
    incident_nums: 4000,
    most_incident_type: 'Vehicle Fire',
    month_incident: [150, 100, 230, 102, 232, 121, 233, 111, 221, 322, 400],
    year_incident: {
        years: [2021, 2022, 2023, 2024],
        incident_nums: [1200, 942, 729, 1250]
    }
})

const data = ref({
    incident: 210,
    avg_resolve: 3.15,
    incident_type: [
        'Vehicle Fire',
        'Search and Rescue',
        'Structure Fire',
        'HAZMAT Fire',
    ],
    incident_nums: [120, 20, 5, 1]
})

const firstYear = computed(() => {
    return overallData.value.year_incident.years[0]
})

const lastYear = computed(() => {
    return overallData.value.year_incident.years[
        overallData.value.year_incident.years.length - 1
    ]
})

// const fetchData = async() => { ADD CODE TO FETCH DATA HERE }

</script>