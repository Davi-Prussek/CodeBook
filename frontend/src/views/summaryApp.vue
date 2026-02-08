<script setup>
import { useRouter, RouterLink } from 'vue-router'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const router = useRouter()
const listaRotas = router.getRoutes()
</script>

<template>
<div class="body">
    <ul>
    <li v-for="rota in listaRotas.slice(1,4)" :key="rota.name">
      <RouterLink :to="rota.path" :style="{color: rota.meta.color}">
        {{ rota.name }} <font-awesome-icon class="icone" :icon="rota.meta.icon" :style="{ color: rota.meta.color }"/>
      </RouterLink>
    </li>
  </ul>
</div>
</template>
<style scoped>
.body {
  margin: 0vw;
  background-color: black;
  ul {
    margin-top: 20%;
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 2vw;
    li {
      border-radius: 24px;
      box-shadow: 0px 0px 15px 10px rgba(0, 0, 0, 0.372);
      cursor: pointer;
      background-color: rgb(0, 0, 0);
      transition: all ease 0.9s;
      a {
        padding: 0.5vw;
        text-decoration: none;
        display: flex;
        flex-direction: column-reverse;
        align-items: center;
        .icone {
          font-size: 5vw;
        }
      }
    }
    li:hover{
      transform: scale(1.25);
    }
  }
}
</style>
