import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueAxios from 'vue-axios'
import axios from 'axios'


Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  beforeCreate() {
    this.$store.dispatch("loginRefresh")
  },
  render: h => h(App),
}).$mount('#app');
