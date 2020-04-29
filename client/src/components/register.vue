<template >
<div class="admin-container2">
  <div class="container-fluid" >
    <div class="register">
                <form @keydown.enter="register({Email,password,passwordConfirm,username})">
                <div class="email">
                 Type your E-mail
                </div>
                    <div class="form-group">
                        <input type="text" style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="Email" name="Email" placeholder="Email">
                    </div>
                    <div class="password">
                    Type your Password
                    </div>
                    <div class="form-group">
                        <input type="password" style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="password" name="password"  placeholder="Password">
                    </div>
                    <div class="form-group">
                        <input type="password" style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="passwordConfirm" name="passwordConfirm" placeholder="Password Check" >
                    </div>
                    <div class="name">
                    Type your name
                    </div>
                    <div>
                        <input type="text" style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="username" name="username" placeholder="Name">
                    </div>
                </form>
                <br>
                <br>
                <button @click="register({Email,password,passwordConfirm,username})" style="color:white; background-color: #f9bd5bm; width:400px; height:60px; font-weight:bold; font-size:31px;" class="btn btn-warning btn-block">S I G N &nbsp;  U P</button>
                <br>
                <div class= "question">
                  <a href="/login" style="color:white;">Sign in here</a>
                </div>
            </div>
             </div>
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
        ...mapActions(["register"]),




    }
}
</script>

<style>
    .register {
      position: absolute;
        top: 15%;
        left: 30%;
        padding-top: 5%;
        padding-bottom: 5%;
        padding-right: 10%;
        padding-left: 10%;
    }
    .email {
    position:relative;
          top:-5px;
          left: -125px;
          text-align: center;
          font-size: 1.2em;
          color:white;
          line-height: 2em;
    }
     .password {
    position:relative;
          top:-5px;
          left: -110px;
          text-align: center;
          font-size: 1.2em;
          color:white;
          line-height: 2em;
    }
    .name {
     position:relative;
          top:-5px;
          left: -130px;
          text-align: center;
          font-size: 1.2em;
          color:white;
          line-height: 2em;
    }
</style>
