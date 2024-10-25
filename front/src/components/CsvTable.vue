<script setup>
import { VDataTable } from 'vuetify'

const items = [
    {
      name: 'African Elephant',
      species: 'Loxodonta africana',
      diet: 'Herbivore',
      habitat: 'Savanna, Forests',
    },
  ]
</script>

<template>
    <h1>CSV</h1>
    <v-data-table :items="items"></v-data-table>
</template>