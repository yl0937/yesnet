<template>
  <div id="app">
    <div class="admin-container">
      <div class="Header">
         <Header/>
      <div class="sidebar">
          <sidebar/>
      <div id="right-panel" class= "right-panel">
        <div class="content pb-o">
          <transition enter-active-class="animated fadeIn">
            <router-view></router-view>
          </transition>
         </div>
</div>
</div>
</div>
</div>
</div>
</template>

<script>
import { mapState, mapActions} from "vuex"
import Header from './uxcomponents/Header.vue'
import sidebar from './uxcomponents/sidebar.vue'
import Home from './components/Home.vue'


export default {
  data(){
    return{
    }
  },
  components:{
    Header,
    sidebar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.content {
    float: left;
    padding: 1.875em;
    width: 100%;
}
</style>
