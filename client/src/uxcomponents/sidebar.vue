<template>

    <aside id="left-panel" class="left-panel"   >
               <nav class="navbar navbar-expand-sm navbar-default">

            <SidebarHeader/>

            <div id="main-menu" class="main-menu collapse navbar-collapse">
                <ul class="nav navbar-nav">
                  <li class="nav-item">
                  <h6 class="header-item ">
                  <span>DAPPS</span>
                  </h6>
                  </li>
                  <li class="nav-item">
                      <router-link class="nav-link" to="/DAppsUpload">
                       <img src="../images/dappsupload.png" style="position:relative; top:-1px; left:-10px;">DApps Upload
                  </router-link>
                  </li>
                  <li class="nav-item">
                  <router-link class="nav-link" to="/DAppsList">
                  <img src="../images/dappslist.png" style="position:relative; top:-1px; left:-10px;">DApps List
                  </router-link>
                  </li>
                  <li class="nav-item">
                  <router-link class="nav-link" to="/DeployedDApps">
                  <img src="../images/deployeddapps.png" style="position:relative; top:-6px; left:-10px;">Deployed DApps
                  </router-link>
                  </li>


                  <h6 class="header-item ">
                  <span>WATCHERS</span>
                  </h6>
                  <ul class="nav ">
                  <li class="nav-item">
                  <router-link class="nav-link" to="/WatchBlock">
                  <img src="../images/watchblock.png" style="position:relative; top:-3px; left:-10px;">Watch Block
                  </router-link>
                  </li>
                  <li class="nav-item">
                  <router-link class="nav-link" to="/WatchTX">
                  <img src="../images/watchtx.png" style="position:relative; top:-6px; left:-10px;">Watch TX
                  </router-link>
                  </li>
                  </ul>


                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>
    </aside><!-- /#left-panel -->

</template>



<script>
import { mapState, mapActions } from "vuex"
import SidebarHeader from './sidebar/SidebarHeader.vue';
import SidebarNavDropdown from './sidebar/SidebarNavDropdown.vue';
import SidebarNavTitle from './sidebar/SidebarNavTitle.vue';
import SidebarNavLink from './sidebar/SidebarNavLink.vue';
import SidebarNavItem from './sidebar/SidebarNavItem.vue';
import SidebarFooter from './sidebar/SidebarFooter.vue';
import Vue from 'vue';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);


export default{
    name: 'sidebar',
    props: {
        navItems: {
          type: Array,
          required: true,
          default: () => []
      }
    },
   computed: {
        ...mapState(["isLogin"])
    },
    components: {
        SidebarHeader,
        SidebarNavDropdown,
        SidebarNavLink,
        SidebarNavTitle,
        SidebarNavItem,
        SidebarFooter
    },
    methods: {
        handleClick (e) {
          e.preventDefault()
          e.target.parentElement.classList.toggle('show')
      }
    }
}
</script>
<style>
.sidebar {
position: fixed;
top: 10%;
bottom: 0;
left: 0;
z-index: 100; /* Behind the navbar */
padding: 48px 0 0; /* Height of navbar */
box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

.sidebar-sticky {
position: relative;
top: 0;
height: calc(100vh - 48px);
padding-top: .5rem;
overflow-x: hidden;
overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

@supports ((position: -webkit-sticky) or (position: sticky)) {
.sidebar-sticky {
position: -webkit-sticky;
position: sticky;
}
}

.sidebar .nav-link {
font-weight: 300;
color: #333;
}

.sidebar .nav-link .feather {
margin-right: 20px;
color: #999;
}

.sidebar .nav-link.active {
color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
color: inherit;
}

.sidebar-heading {
font-size: .75rem;
text-transform: uppercase;
}
.header-item{
  font-size: 1.50rem;
  font-weight: bold;
  font-family:  'Avenir', Helvetica, Arial, sans-serif;
  margin-top: 40px;
  margin-left: 30px;
}
.icon1{
   top:20%;
  left:-30%;

  }
</style>
