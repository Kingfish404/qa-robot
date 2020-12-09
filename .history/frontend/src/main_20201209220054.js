import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import { createApp } from 'vue'

Vue.config.productionTip = false

Vue.use(Buefy)

createApp(App).use(store).usemout