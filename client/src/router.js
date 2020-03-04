import Vue from 'vue';
import Router from 'vue-router';
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
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/DAppsUpload',
      name: 'DAppsUpload',
      component: DappUpload,
    },
    {
      path: '/DAppsList',
      name: 'DAppsList',
      component: DAppsUpList,
    },
    {
      path: '/Dashboard',
      name: 'DashBoard',
      component: Dashboard,
    },
    {
      path: '/DeployedDApps',
      name: 'DeployedDApps',
      component: DeployedDApps,
    },
    {
      path: '/WatchBlock',
      name: 'WatchBlock',
      component: WatchBlock,
    },
    {
      path: '/WatchTX',
      name: 'WatchTx',
      component: WatchTX,
    },
  ],
});
