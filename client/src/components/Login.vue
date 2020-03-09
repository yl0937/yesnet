<style>



    .test12 {
        position: absolute;
        top: 20%;
        left: 33%;

        padding-top: 5%;
        padding-bottom: 5%;
        padding-right: 10%;
        padding-left: 10%;
        vertical-align: middle;
        border: #f7b642 solid 5px;
    }
</style>

<template>
  <div class="container-fluid"  id="cm">
    <div class="high" >

        <div class="test12">
            <form>
                <div class="form-group">
                    <label>User E-mail</label>
                    <input type="text" class="form-control" v-model="email" name="email" placeholder="Email">
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" class="form-control" v-model="password" name="password" placeholder="Password">
                </div>
            </form>

            <button @click="login({ email, password})" class="btn btn-warning btn-block"

            >Login</button>
            <br>
            <div>
                Don't have an account? <a href="/register">Sign up here</a>.
            </div>`
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
