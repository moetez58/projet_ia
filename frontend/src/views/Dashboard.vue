<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Dashboard Immobilier</h1>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-600">Chargement...</p>
    </div>
    
    <div v-else-if="error" class="bg-red-100 text-red-700 p-4 rounded">
      {{ error }}
    </div>
    
    <div v-else>
      <!-- KPIs -->
      <StatsCard v-if="stats" :stats="stats" />
      
      <!-- Graphique -->
      <div class="mb-6">
        <PriceChart :data="chartData" />
      </div>
      
      <!-- Tableau -->
      <DataTable v-if="data" :columns="data.columns" :rows="data.rows" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { fetchData, fetchStats } from '../services/api';
import type { ApiData, Stats, Property } from '../types';
import DataTable from '../components/DataTable.vue';
import StatsCard from '../components/StatsCard.vue';
import PriceChart from '../components/PriceChart.vue';

const data = ref<ApiData | null>(null);
const stats = ref<Stats | null>(null);
const loading = ref(true);
const error = ref('');

const chartData = computed<Property[]>(() => {
  if (!data.value) return [];
  return data.value.rows.map(row => ({
    surface: Number(row[0]),
    chambres: Number(row[1]),
    prix: Number(row[2])
  }));
});

const loadData = async () => {
  try {
    loading.value = true;
    const [dataResponse, statsResponse] = await Promise.all([
      fetchData(),
      fetchStats()
    ]);
    data.value = dataResponse;
    stats.value = statsResponse;
  } catch (err) {
    error.value = 'Erreur de connexion à l\'API';
    console.error(err);
  } finally {
    loading.value = false;
  }
};

onMounted(loadData);
</script>