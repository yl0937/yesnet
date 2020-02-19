import Vue from 'vue';
import Router from 'vue-router';
import Books from './components/Books.vue';
import Ping from './components/Ping.vue';
import Main from './components/Main.vue';
import Tiki from './components/Tiki.vue';
import Login from './components/Login.vue';
import Dapp from './components/Dapp.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Main',
      component: Main,
    },
    {
      path: '/tiki',
      name: 'tiki',
      component: Tiki,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/dapp',
      name: 'Dapp',
      component: Dapp,
    },
  ],
});
