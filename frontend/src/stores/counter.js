import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useColorStore = defineStore('color', () => {
  const preto = ref('#000000')
  const branco = ref('#ffffff')
  function trocarCor() {
    const preto1 = ref(preto.value);
    preto.value = branco.value;
    branco.value = preto1.value;
  }

  return { preto, branco,trocarCor }
})
