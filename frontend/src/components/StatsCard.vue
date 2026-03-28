<template>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
    <div v-for="stat in statsList" :key="stat.label" class="bg-white rounded-lg shadow p-4">
      <p class="text-sm text-gray-500 uppercase">{{ stat.label }}</p>
      <p class="text-2xl font-bold text-blue-600">{{ stat.value }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { Stats } from '../types';

const props = defineProps<{
  stats: Stats;
}>();

const statsList = computed(() => [
  { label: 'Prix moyen', value: `${Math.round(props.stats.mean_prix || 0).toLocaleString('fr-FR')} €` },
  { label: 'Surface moyenne', value: `${props.stats.mean_surface} m²` },
  { label: 'Chambres moy.', value: props.stats.mean_chambres },
  { label: 'Corrélation', value: props.stats.correlation },
]);
</script>