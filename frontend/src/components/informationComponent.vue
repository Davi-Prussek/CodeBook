<script setup>
import { useRouter } from 'vue-router';
import axios from 'axios';

import { onMounted, ref } from 'vue';
const router = useRouter()
const rotaAtual = router.currentRoute.value.name
const categorias = ref([]);

onMounted(async () => {
const response = await axios.get(`https://codebook-k7oo.onrender.com/categorias/`)
categorias.value = response.data;
});
</script>
<template>
A rota atual é: {{ rotaAtual }}

Aqui tem as informações sobre as seguintes categorias:

<ul>
  <li v-for="(item, index) in categorias" :key="index">
    nome: {{ item.nome }}
  </li>
</ul>
</template>
