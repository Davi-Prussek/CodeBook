import { createRouter, createWebHistory } from 'vue-router'
import HTML from '@/views/HTML.vue'
import CSS from '@/views/CSS.vue'
import JS from '@/views/JS.vue'
import summary from '@/views/summaryApp.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faHtml5, faCss3Alt, faJsSquare } from '@fortawesome/free-brands-svg-icons'

library.add(faHtml5,faCss3Alt,faJsSquare)

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'sumário',
      component: summary,
    },
    {
      path: '/html',
      name: 'HTML',
      component: HTML,
      meta: {
        icon: ['fab', 'html5'],
        color: '#E34F26',
        shadowColor: 'rgba(227, 79, 38, 0.34)'
      }
    },
    {
      path: '/css',
      name: 'CSS',
      component: CSS,
      meta: {
        icon: ['fab', 'css3-alt'],
        color: '#1572B6',
        shadowColor: 'rgba(21, 114, 182, 0.34)'
      }
    },
    {
      path: '/js',
      name: 'JS',
      component: JS,
      meta: {
        icon: ['fab', 'square-js'],
        color: '#F7DF1E',
        shadowColor: 'rgba(247, 223, 30, 0.34)'
      }
    },
  ],
})

export default router
