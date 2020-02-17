<template>
<form class="form-Login">
  <h1 class="h3 mb-3 font-weight-normal">Please Login</h1>
  <label for="email" class="sr-only">Email address</label>
  <input type="email" id="email" v-model="email" class="form-control" placeholder="Email address" required autofocus>
  <label for="password" class="sr-only">Password</label>
  <input type="password" id="password" v-model="password" class="form-control" placeholder="Password" required>
  <div class="checkbox mb-3">
    <label>
      <input type="checkbox" value="remember-me"> Remember me
    </label>
  </div>
  <button @click="login({ email, password})" class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
  <p class="mt-5 mb-3 text-muted"></p>
</form>

</template>


<script>
import { mapState, mapActions } from "vuex"
import axios from 'axios';

export default {
    data() {
        return{
            email: null,
            password: null
            }
    },
    computed: {
            ...mapState(["isLogin", "isLoginError"])
    },
    methods: {
        ...mapActions(["login"]),

            }
}


</script>

<style scoped>

body {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-Login {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}
.form-Login .checkbox {
  font-weight: 400;
}
.form-Login .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-Login .form-control:focus {
  z-index: 2;
}
.form-Login input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-Login input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
