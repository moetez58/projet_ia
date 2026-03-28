<template>
  <div class="bg-white rounded-lg shadow overflow-hidden">
    <h2 class="text-xl font-bold p-4 bg-gray-100">Liste des biens immobiliers</h2>
    <table class="w-full">
      <thead class="bg-gray-50">
        <tr>
          <th v-for="col in columns" :key="col" class="px-4 py-2 text-left font-semibold text-gray-700">
            {{ col }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in rows" :key="index" class="border-t hover:bg-gray-50">
          <td v-for="(cell, cellIndex) in row" :key="cellIndex" class="px-4 py-2">
            {{ formatCell(cell) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  columns: string[];
  rows: (string | number)[][];
}>();

const formatCell = (cell: string | number): string => {
  if (typeof cell === 'number') {
    return cell.toLocaleString('fr-FR');
  }
  return cell;
};
</script>