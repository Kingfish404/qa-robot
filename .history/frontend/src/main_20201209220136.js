import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import { createApp } from 'vue'


createApp(App).use(store).use(Buefy).mount('#app')