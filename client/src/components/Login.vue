<style>
 .login {
        position: absolute;
        top: 33%;
        left: 40.3%;
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
          transform: translate( 95%,20%);
          border-radius: 15px;
        }
.title {
          z-index:5;
          position:relative;
          width: 800px;
          margin: 0 auto;
          top:210px;
          left: -10px;
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

<template>
  <div class="container-fluid" >
  <div class="title">
            <b><span class="accent">SIGN IN</span></b>
  </div>
          <div class="box"></div>
          <div class="login">
            <form>
                <div class="form-group">
                    <input type="text" style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="email" name="email" placeholder="Email">
                </div>
                <div class="form-group">
                    <input type="password"  style="background-color:transparent; width:400px; height:50px;" class="form-control" v-model="password" name="password" placeholder="Password">
                </div>
            </form>
            <br>
            <button @click="login({ email, password})" class="btn btn-warning btn-block" style="color:white; background-color: #f9bd5bm; width:400px; height:60px; font-weight:bold; font-size:31px;" >L O G   I N </button>
            <br>
            <br>
            <br>
            <br>
            <div class= "question">
              <a href="/register" >Sign up here</a>
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
