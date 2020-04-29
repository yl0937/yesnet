<template>
        <header id="basix-header" class="header" v-show="isLogin" >

            <div class="header-menu" >

                <div class="row">
                    <div class="col-sm-7">

                        <div class="header-left" :class="{'open': isSearch, '': !isSearch }">
                            <input class="form-control form-control-dark w-0" type="text" placeholder="Search" aria-label="Search">

                            <div class="form-inline">
                                <form class="search-form">
                                    <input class="form-control mr-sm-2" type="text" placeholder="Search ..." aria-label="Search">
                                    <button
                                        class="search-close"
                                        type="submit"
                                        @click="isSearch = !isSearch"
                                    ><i class="fa fa-close"></i></button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-5" v-if="isLogin" style="position:fixed; right:15px; top:15px;">
                        <div class="user-area dropdown float-center"  >
                            <div>
                                <img class="btn btn-default dropdown-toggle" style="position:fixed;"
                                     src="../images/userIcon.png"  alt="User Avatar"
                                     data-toggle="dropdown"
                                     class="img-thumbnail" width="50" height="50"
                                     class="img-circle"
                                >
                            </div>
                            <div
                                class="user-menu dropdown-menu"
                                float="right;">
                                <a class="nav-link" href="#"><i class="fa fa- user"></i>my profile</a>

                                <a class="nav-link" href="#"  @click="logout" ><i class="fa fa-power -off"></i>Sign out</a>
                            </div>

                        </div>
                    </div>
                </div>

            </div>

        </header><!-- /header -->
</template>


<script>
import { mapState, mapActions } from "vuex"
    export default {
    name: 'basix-header',
    data (){
      return{
        isActive: false,
        isFlag: false,
        isMessage: false,
        isNotification: false,
        isSearch: false,
        isOpen: false
      }
    },
    computed: {
        ...mapState(["isLogin"])
    },
    methods: {
        ...mapActions(["logout"]),
        toggle(e){
            //this.isOpen = !this.isOpen
            e.target.parentElement.classList.toggle('close')
        },
        handleClick(e){
            this.isActive = !this.isActive;
            // if(e.target.className == "noclass"){
            //     e.target.className = "link active";
            // } else{
            //     e.target.className = "noclass";
            // }
        },
        searchClick (e) {
          this.isSearch = !this.isSearch;
        },
        handleMessage (e) {
          this.isMessage = !this.isMessage;
        },
        handleNotification (e) {
          this.isNotification = !this.isNotification;
        },
        handleFlag (e) {
          this.isFlag = !this.isFlag;
        }

      }
    }
</script>

<style>
    header .form-inline .search-form button{
        cursor: pointer;
    }

    .dropdown:hover .dropdown-menu{
        background:rgba(0,0,0,0.08);
        display: block;
        margin-top: -5px;
    }
</style>
