import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueChartJs from 'vue-chartjs'

Vue.config.productionTip = false
Vue.use(VueChartJs)

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')