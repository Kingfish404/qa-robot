import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import Vue from 'vue'


Vue.use(Buefy)

new Vue({
  render: h => h(App),
}).$mount('#app')