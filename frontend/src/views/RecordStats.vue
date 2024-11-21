<template>
    <div class="pt-4 px-4">
        <h1 class="text-4xl font-bold mb-6">
            Record Stats
        </h1>
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
    </div>
</template>

<script setup>
import { ref } from 'vue'

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

// const fetchData = async() => { ADD CODE TO FETCH DATA HERE }

</script>