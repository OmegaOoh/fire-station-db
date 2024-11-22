<template>
    <div class="pt-4 px-4">
        <h1 class="font-extrabold text-5xl">Overall</h1>
        <div class="flex w-full flex-col my-6">
            <div class="stats bg-base-200 shadow w-full mb-4">
                <div class="stat place-items-center">
                    <div class="stat-title">Dispatch Response</div>
                    <div class="stat-value">{{ overallData.responded }}</div>
                    <div class="stat-desc text-secondary font-semibold text-lg"></div>
                </div>

                <div class="stat place-items-center">
                    <div class="stat-title">Most Dispatch Type</div>
                    <div class="stat-value text-secondary">{{ overallData.mostType }}</div>
                    <div class="stat-desc text-secondary font-semibold text-lg">{{ overallData.mostPercentage }} %</div>
                </div>

                <div class="stat place-items-center">
                    <div class="stat-title">Fire Fighter on Duty</div>
                    <div class="stat-value">{{ overallData.activeDuty }}</div>
                    <div class="stat-desc text-base-content font-semibold text-lg">across {{ overallData.stations_num }} stations </div>
                </div>
            </div>
            <div class="stats bg-base-200 shadow w-full">
                <div class="stat place-items-center" v-for="(data, index) in overallData.byMonth" :key="data.month">
                    <div class="stat-title">{{ data.month }}</div>
                    <div class="stat-value" :class="colorByIndex(index)">{{ data.dispatch }}</div>
                    <div class="stat-desc">Dispatched</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue';

const overallData = ref({
    responded: 2015,
    mostType: "Vehicle Fire",
    mostPercentage: 42,
    stations_num: 5,
    activeDuty: 30,
    byMonth: [
        {month: 'Jan', dispatch: 230},
        {month: 'Feb', dispatch: 120},
        {month: 'Mar', dispatch: 100},
        {month: 'Apr', dispatch: 120},
        {month: 'May', dispatch: 200},
        {month: 'Jun', dispatch: 300},
        {month: 'Jul', dispatch: 123},
        {month: 'Aug', dispatch: 200},
        {month: 'Sep', dispatch: 90},
        {month: 'Oct', dispatch: 84},
        {month: 'Nov', dispatch: 242},
        {month: 'Dec', dispatch: 431},
    ]
})

const colorByIndex = (index) => {
    return index % 2 == 0 ? '' : 'text-primary'
}
</script>