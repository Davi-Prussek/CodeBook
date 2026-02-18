<script setup>
import { useRouter } from 'vue-router';
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
  } catch {
    console.log('Não foi possível buscar os dados sobre as categorias');
  }

  try {
    const response = await axios.get(`https://codebook-k7oo.onrender.com/Codigos/?categoria__linguagem=${rotaAtual.toLowerCase()}`)
    codigos.value = response.data.results;
    await nextTick()
    Prism.highlightAll();
  } catch {
    console.log('Não foi possível buscar os dados sobre os códigos');
  };
});

const orderingByID = computed(() => {
  return [...codigos.value].sort((a, b) => a.id - b.id);
})
</script>

<template>
  <headerComponent />

  <div class="main">
    <div class="categorias">
      <button v-for="(item, index) in categorias" :key="index">
        {{ item.nome }}
        <p>{{ item.descricao }}</p>
      </button>
    </div>
    <section class="codigos">
      <ul>
        <li v-for="(item, index) in orderingByID" :key="index">
          <h3>{{ item.nome }}</h3>
          <pre>
            <code :class="rotaAtual === 'html' ? 'language-html' : rotaAtual === 'css' ? 'language-css' : 'language-js'">
              {{ item.modoDeUsar }}
            </code>
          </pre>
          <p>{{ item.descricao }}</p>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.main {
  display: flex;
  height: 100vh;
  gap: 20px;
  box-sizing: border-box;
  padding-top: 4vw;
.categorias {
  width: 15%;
  height: 100%;
  overflow-y: auto;
  border-right: 1px solid rgb(184,184,184);
  display: flex;
  flex-direction: column;
  gap: 10px;
  background-color: #fff;
  box-sizing: border-box;
  z-index: 5;
  padding-inline: 15px;
button {
  position: relative;
  background: transparent;
  border: none;
  font-size: 16px;
  padding: 8px 10px;
  border-radius: 5px;
  text-align: left;
  cursor: pointer;
 p {
  position: absolute;
  left: 120px;
  top: 0;
  background: #000;
  color: #fff;
  padding: 5px 10px;
  border-radius: 6px;
  display: none;
  white-space: nowrap;
  font-size: 14px;
  z-index: 100;
}

&:hover p {
  display: block;
}

&:hover {
  background-color: rgb(224,224,224);
}}}

.codigos {
  padding-inline: 15px;
  flex: 1;
  height: 100%;
  overflow-y: auto;
  ul {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(1 2fr);
  gap: 1vw;
  li {
    flex: 1;
    pre {
      margin: 0;
      padding: 0;
      text-align: center;
      border-radius: 10px;
    code {
      margin: 0;
      padding: 0;
    }
    }
  }
}}}
</style>
