<script setup>
import {useRouter} from 'vue-router';
import axios from 'axios';
import { computed, nextTick, onMounted, ref } from 'vue';
import Prism from 'prismjs';
import headerComponent from './headerComponent.vue';

const router = useRouter()
const rotaAtual = router.currentRoute.value.name
const codigos = ref([]);
const categorias = ref([]);

onMounted(async () => {

  try {
    const response = await axios.get(`https://codebook-k7oo.onrender.com/Categorias/?linguagem=${rotaAtual.toLowerCase()}`);
    categorias.value = response.data.results;
    console.log(response.data)
  }
  catch {
    console.log('Não foi possível buscar os dados sobre as categorias')
  }

  try {
    const response = await axios.get(`https://codebook-k7oo.onrender.com/Codigos/?categoria__linguagem=${rotaAtual.toLowerCase()}`)
    codigos.value = response.data.results;
    await nextTick()
    Prism.highlightAll();
  }
  catch {
    console.log('Não foi possível buscar os dados sobre os códigos')
  };

});

const orderingByID = computed(() => {
  return [...codigos.value].sort((a,b)=>a.id-b.id);
})

/* function filtrar() {} */
</script>
<template>
<headerComponent/>
<div class="categorias">
<ul>
  <li v-for="(item,index) in categorias" :key="index">
     {{ item.nome }}
     <p>{{ item.descricao }}</p>
      </li>
     </ul>
</div>
</template>
<style scoped>
.categorias {
  height: max-content;
  width: min-content;
  border-right: 2px solid black;
  ul {
    display: flex;
    flex-direction: column;
    gap: 1vw;
    li {
      padding-inline: 0.5vw;
    }
  }
}
</style>
