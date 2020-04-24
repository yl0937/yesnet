<template>
  <div id="app" >
    <auth-layout ></auth-layout>
      <div class="admin-container">
          <sidebar :navItems="nav"/>
            <div id="right-panel"  class="right-panel">
            <Header/>
            <div class="content pb-0">
              <transition enter-active-class="animated fadeIn">
                <router-view></router-view>
              </transition>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
import nav from './uxcomponents/nav.js'
import Header from './uxcomponents/Header.vue'
import sidebar from './uxcomponents/sidebar.vue'
import Home from './components/Home.vue'


export default {
    data () {
        return {
            nav: nav.items
        }
    },
  computed: {
        ...mapState(["isLoginError"])
    },
    components: {
        Header,
        sidebar
    }
}
</script>

<style>
@import url('./assets/style.scss');

.content {
    float: left;
    display: table;
    background-color: #fdfbfd;
  position: absolute;
  top:80px;
  left: 290px;
  width:85%;


}
</style>
