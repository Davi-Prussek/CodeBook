<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
const rotaAtual = router.currentRoute.value.name
</script>
<template>
  <RouterLink to="/">Início</RouterLink>
  <p>Aqui irá conter os dados sobre: {{ rotaAtual }}</p>
</template>
