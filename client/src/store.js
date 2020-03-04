import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import axios from 'axios'
import {isNull} from "bootstrap-vue/esm/utils/inspect";
import {from} from "bootstrap-vue/esm/utils/array";

// test it.
Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        userInfo: null,
        isLogin: false,
        isLoginError: true
    },
    mutations: {
        //login success
        loginSuccess(state){
            state.isLogin = true,
            state.isLoginError = false
        },
        //login fail
        loginError(state){
            state.isLogin = false,
            state.isLoginError = true
        },
        logout(state) {
            state.isLogin = false,
            state.isLoginError = false,
            sessionStorage.removeItem("access_token");

        }
    },
    actions:{
        //try login
        login({ commit}, loginObj) {
            // Login => token return
            axios
                .post("http://localhost:5000/api/login", loginObj)
                .then(res => {
                  console.log("test")
                    let response = res.data
                    console.log(response)
                    if(response['code'] == '200')
                        {
                        sessionStorage.setItem("access_token", response['access_token'])
                        let token = sessionStorage.getItem("access_token")
                        let config = {
                            headers: {
                                "Authorization": token
                                }
                            }
                            commit('loginSuccess')
                            router.push("/watchblock")
                        }
                    else {
                        alert(' Check your Id&PW 1');
                        }
                })
                .catch(() => {
                           alert(' Check your Id&PW 2');
                       })
            },
        register({ commit }, registerObj) {
            if (registerObj['password'] == registerObj['passwordConfirm'])
            {
            axios
                .post("http://localhost:5000/api/register", registerObj)
                .then(res => {
                    let response = res.data
                    {
                        console.log(response)
                        if (response['code'] == '404') {
                            alert(' Already exist ID')
                        } else {
                            alert(' Register Success')
                            router.go(-1)
                        }
                    }
                })
            }
            else {
                alert('password is not same')
            }
        },
        logout({commit}) {
                commit("logout")
                router.push("/login")
            },
    }
})
