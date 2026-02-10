<script setup>
import { useRouter, RouterLink } from 'vue-router'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const router = useRouter()
const listaRotas = router.getRoutes()
</script>

<template>
<div class="body">
    <ul>
    <li v-for="rota in listaRotas.slice(1,4)" :key="rota.name" :style="{boxShadow: `0px 0px 15px 10px ${rota.meta.shadowColor}`}">
      <RouterLink :to="rota.path" :style="{color: rota.meta.color}">
        <p>{{ rota.name }}</p> <font-awesome-icon class="icone" :icon="rota.meta.icon" :style="{ color: rota.meta.color }"/>
      </RouterLink>
    </li>
  </ul>
</div>
</template>
<style scoped>
.body {
  ul {
    margin-top: 20%;
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 3.5vw;
    li {
      border-radius: 24px;
      cursor: pointer;
      background-color: #ffffff;
      transition: all ease 0.9s;
      a {
        padding-inline: 4vw;
        padding-top: 1.5vw;
        padding-bottom: 1vw;
        text-decoration: none;
        font-size: 2vw;
        display: flex;
        flex-direction: column-reverse;
        align-items: center;
        .icone {
          font-size: 7vw;
        }
        p {
          font-size: 2vw;
        }
      }
    }
    li:hover{
      transform: scale(1.25);
    }
  }
}
</style>
