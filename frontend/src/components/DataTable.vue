<template>
  <div class="bg-white rounded-lg shadow overflow-hidden">
    <h2 class="text-xl font-bold p-4 bg-gray-100">Liste des biens immobiliers ({{ rows.length }})</h2>
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead class="bg-gray-50">
          <tr>
            <th v-for="col in columns" :key="col" class="px-4 py-2 text-left font-semibold text-gray-700 uppercase text-sm">
              {{ col }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in rows" :key="index" class="border-t hover:bg-blue-50 transition">
            <td v-for="(cell, cellIndex) in row" :key="cellIndex" class="px-4 py-3">
              <span v-if="cellIndex === 2" class="font-semibold text-green-600">
                {{ formatPrice(cell) }}
              </span>
              <span v-else-if="cellIndex === 0" class="font-medium">
                {{ cell }} m²
              </span>
              <span v-else>
                {{ cell }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  columns: string[];
  rows: (string | number)[][];
}>();

const formatPrice = (price: number | string): string => {
  const num = typeof price === 'string' ? parseInt(price) : price;
  return num.toLocaleString('fr-FR') + ' €';
};
</script>