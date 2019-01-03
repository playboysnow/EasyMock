import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import mock from '@/components/mock'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
     name: 'HelloWorld',
     component: HelloWorld
    },
    {
      path: '/mock',
      name: 'mock',
      component: mock
    }
    
  ]
})
