<script setup>
import { useRouter,RouterLink } from 'vue-router';
import axios from 'axios';
import { nextTick, onMounted, ref } from 'vue';
import Prism from 'prismjs';

const router = useRouter()
const rotaAtual = router.currentRoute.value.name
const categorias = ref([]);
/* const filtro = ref(''); */

onMounted(async () => {

  try {
    const response = await axios.get(`https://codebook-k7oo.onrender.com/Codigos/?categoria__linguagem=html&page=1`)
    categorias.value = response.data.results;
    await nextTick()
    Prism.highlightAll();
  }
  catch {
    console.log('Não foi possível fazer o requerimento via render')
  };

/*   ?categoria__linguagem=${rotaAtual.toLowerCase()} */
/*   try {
    const response = await axios.get(`http://127.0.0.1:8000/Codigos/`)
    categorias.value = response.data.results;
    await nextTick()
    Prism.highlightAll();
  }
  catch {
    console.log('Não foi possível fazer o requerimento via localhost')
  }; */
});
</script>
<template>
  <RouterLink to="/">Início</RouterLink>
  A rota atual é: {{ rotaAtual }}<br><br>

  Aqui tem as informações sobre as seguintes categorias:

  <ul>
    <li v-for="(item, index) in categorias" :key="index">
      nome: {{ item.nome }}<br>
      id: {{ item.id }}<br>
      categoria: {{ item.categoria.nome }} <br>
        <pre><code :class="item.categoria.linguagem == 'html' ? 'language-html' : item.categoria.linguagem == 'css' ? 'language-css' : 'language-js'">{{ item.modoDeUsar }}</code></pre>
    </li>
  </ul>
</template>
