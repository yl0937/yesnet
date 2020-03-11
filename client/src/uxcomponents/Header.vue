<template>
  <div class="Header">
<nav class="navbar navbar-dark fixed-top bg-color flex-md-nowrap p-10 shadow">
  <a class="navbar-brand col-sm-3 col-md-2 mr-10" href="/"><img src="../images/logo.png" alt="Logo"></a>
  <input class="form-control form-control-dark w-0" type="text" placeholder="Search" aria-label="Search">
  <ul class="navbar-nav px-3">
    <li class="nav-item text-nowrap">
      <a class="nav-link" @click="logout()" href="#">Sign out</a>
    </li>
  </ul>
</nav>
</div>
</template>


<script>
import { mapState, mapActions } from "vuex"
  export default {
    data() {
    },
    computed: {
            ...mapState(["isLogin", "isLoginError"])
    },
    methods: {
        ...mapActions(["logout"]),

            }
}
</script>
<style scoped>
body {
  font-size: .875rem;
}

.feather {
  width: 16px;
  height: 16px;
  vertical-align: text-bottom;
}

/* 사이드바 색상 */
.bg-color{
background-color: #5b4470;
}

</style>
