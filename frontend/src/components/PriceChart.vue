<template>
  <div class="bg-white rounded-lg shadow p-4">
    <h2 class="text-xl font-bold mb-4">Prix vs Surface</h2>
    <div class="h-64">
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const props = defineProps<{
  data: { surface: number; prix: number }[];
}>();

const chartCanvas = ref<HTMLCanvasElement | null>(null);
let chart: Chart | null = null;

const createChart = () => {
  if (!chartCanvas.value || props.data.length === 0) return;
  
  if (chart) chart.destroy();

  chart = new Chart(chartCanvas.value, {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'Biens immobiliers',
        data: props.data.map(d => ({ x: d.surface, y: d.prix })),
        backgroundColor: 'rgba(59, 130, 246, 0.6)',
        borderColor: 'rgba(59, 130, 246, 1)',
        pointRadius: 6,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { 
          title: { display: true, text: 'Surface (m²)' },
          type: 'linear',
          position: 'bottom'
        },
        y: { 
          title: { display: true, text: 'Prix (€)' } 
        }
      }
    }
  });
};

onMounted(createChart);
watch(() => props.data, createChart, { deep: true });
</script>