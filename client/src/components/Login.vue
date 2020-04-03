<template>
  <div class="admin-container2">
    <div class="container-fluid" >
      <div class="title">
            <b><span class="accent">SIGN IN</span></b>
      </div>
          <div class="box"></div>
          <div class="login">
            <form @keydown.enter="login({email, password})">
                <div class="form-group">
                    <input type="text" style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="email" name="email" placeholder="Email">
                </div>
                <div class="form-group">
                    <input type="password"  style="background-color:transparent; width:400px; height:50px; " class="form-control" v-model="password" name="password" placeholder="Password">
                </div>
            </form>
            <br>
            <button @click="login({ email, password})" class="btn btn-warning btn-block" style="color:white; background-color: #f9bd5bm; width:400px; height:60px; font-weight:bold; font-size:31px;" >S I G N   I N </button>
            <br>
            <br>
            <br>
            <br>
            <div class= "question">
              <a href="/register" style="color:white;">Sign up here</a>
            </div>
         </div>
      </div>
    </div>
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

<style>
 .login {
        position: absolute;
        top: 30%;
        left: 30%;
        padding-top: 5%;
        padding-bottom: 5%;
        padding-right: 10%;
        padding-left: 10%;
}
 .box{
          z-index:0;
          height:400px;
          width:700px;
          color:#fff;
          background:rgba(0,0,0,0.08);
          padding:50px 0px;
          border-radius: 15px;
          position: absolute;
          top: 15%;
          left: 18.7%;
        }
.title {
          z-index:5;
          position:relative;
          width: 800px;
          margin: 0 auto;
          top:220px;
          left: 0px;
          text-align: center;
          font-size: 4.0em;
          color:white;
          line-height: 2em;
        }
.question{
top: 100%;
left: 20%;
}

</style>
