import Vue from 'vue';
import Router from 'vue-router';
import Books from './components/Books.vue';
import Ping from './components/Ping.vue';
import Tiki from './components/Tiki.vue';
import Login from './components/Login.vue';
import DappUpload from './components/DappUpload.vue';
import DAppsUpList from './components/DAppsList';
import Dashboard from './components/Dashboard';
import DeployedDApps from './components/DeployedDApps';
import Home from "./components/Home";
import WatchBlock from "./components/WatchBlock";
import WatchTX from "./components/WatchTX";

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
      name: 'Home',
      component: Home,
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
      path: '/dappupload',
      name: 'Dapp',
      component: DappUpload,
    },
    {
      path: '/dapplist',
      name: 'DappList',
      component: DAppsUpList,
    },
    {
      path: '/dashboard',
      name: 'DashBoard',
      component: Dashboard,
    },
    {
      path: '/deployeddapps',
      name: 'DeployedDApps',
      component: DeployedDApps,
    },
    {
      path: '/watchblock',
      name: 'WatchBlock',
      component: WatchBlock,
    },
    {
      path: '/watchtx',
      name: 'WatchTx',
      component: WatchTX,
    },
  ],
});
