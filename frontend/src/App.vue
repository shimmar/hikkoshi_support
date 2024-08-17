<script setup>
import { RouterView } from 'vue-router'
import TitleHeader from './components/TitleHeader.vue'
</script>

<template>
  <header>
    <TitleHeader />
  </header>
  <RouterView />
</template>

<style scoped></style>
