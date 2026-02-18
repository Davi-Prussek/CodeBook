<script setup>
import { RouterLink } from 'vue-router';
</script>
<template>
<div>
<RouterLink to='/'>Início</RouterLink>
</div>
</template>
<style scoped>
/* html {
  margin: 0;
  padding: 0;
} */
div {
  border-bottom: 2px solid black;
  position: fixed;
  top: 0;
  width: 100%;
  height: 3vw;
  background-color: white;
  z-index: 10;
  a {
    text-decoration: none;
    font-size: 2.6vw;
    color: black;
  }
}
</style>
