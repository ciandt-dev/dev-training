import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// eslint-disable-next-line no-unused-vars
var appVue = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

window.appVue = appVue
