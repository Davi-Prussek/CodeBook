<script setup>
import headerComponent from './components/headerComponent.vue';
import { RouterView } from 'vue-router';
</script>
<template>
<headerComponent/>
<RouterView/>
</template>
<style scoped>
html {
  margin: 0;
  padding: 0;
}
</style>
