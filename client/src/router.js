import Vue from 'vue';
import Router from 'vue-router';
import store from "./store";
import Login from './components/Login.vue';
import DappUpload from './components/DappUpload.vue';
import DAppsUpList from './components/DAppsList';
import Dashboard from './components/Dashboard';
import DeployedDApps from './components/DeployedDApps';
import Home from "./components/Home";
import WatchBlock from "./components/WatchBlock";
import WatchTX from "./components/WatchTX";

Vue.use(Router);


const rejectAuthUser = (to, from, next) => {
    if (store.state.isLogin === true) {
        alert('Already Login')
        next("/dashboard")
    } else{
        next()
    }
}

const onlyAuthUser = (to, from, next) => {
    if (store.state.isLogin === false) {
        next("/login")
    } else{
        next()
    }
}

export default new Router({
  mode: 'history',
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
      beforeEnter: rejectAuthUser,
    },
    {
      path: '/DAppsUpload',
      name: 'DAppsUpload',
      component: DappUpload,
      beforeEnter: onlyAuthUser,
    },
    {
      path: '/DAppsList',
      name: 'DAppsList',
      component: DAppsUpList,
      beforeEnter: onlyAuthUser,
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
      beforeEnter: onlyAuthUser,
    },
    {
      path: '/WatchBlock',
      name: 'WatchBlock',
      component: WatchBlock,
      beforeEnter: onlyAuthUser,
    },
    {
      path: '/WatchTX',
      name: 'WatchTx',
      component: WatchTX,
      beforeEnter: onlyAuthUser,
    },
  ],
});
