<template>
    <h1>{{ name }}</h1>
  </template>
  
  <script setup lang="ts">
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  const name = route.params.name
  console.log(name)
  </script>
  