import App from './App.vue'
import Buefy from 'buefy'
import Vue from 'vue'


Vue.use(Buefy)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
