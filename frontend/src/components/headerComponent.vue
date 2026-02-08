<script setup>
import { useColorStore } from '@/stores/counter';
const color = useColorStore()
</script>
<template>
<button :style="{backgroundColor: color.preto, color: color.branco}" @click="color.trocarCor">Testando pra ver se eu lembro</button>
</template>
<style scoped>
button {
  position: relative;
  top: 0;
  border: none;
}
</style>
