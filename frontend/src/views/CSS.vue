<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
const rotaAtual = router.currentRoute.value.name
</script>
<template>
<body>
Aqui vai ter as informações sobre: {{ rotaAtual }} 
</body>
</template>
