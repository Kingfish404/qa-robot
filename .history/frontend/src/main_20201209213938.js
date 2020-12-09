import { createApp } from 'vue'
import App from './App.vue'
import Buefy from 'buefy'


Vue.use(Buefy)
createApp(App).mount('#app')

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
