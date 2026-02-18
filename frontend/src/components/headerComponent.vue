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
  border-bottom: 0.5px solid rgb(184, 184, 184);
  position: fixed;
  top: 0;
  width: 100%;
  background-color: white;
  z-index: 10;
  padding: 0.3vw;
  a {
    text-decoration: none;
    font-size: 2.6vw;
    color: black;
  }
}
</style>
