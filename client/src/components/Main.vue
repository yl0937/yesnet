<template>
  <div class="Back">
  <div class="Main">
    <div>
      <router-link to="/login">
      <button class="btn1"><b>SIGN  IN</b></button>
      </router-link>
    </div>
    <div>
      <router-link to="/register">
    <button class="btn2"><b>SIGN  UP</b></button>
        </router-link>
    </div>
    <div class="subtitle">
      <b><span class="accent">YesNet</span>, The Proto Galaxy!</b>
    </div>
    <div class="title">
      <b>Convenient Blockchain Technology!</b>
    </div>
  </div>
    </div>
</template>

<script>
    export default {
        name: "Main"
    }
</script>

<style scoped>
  .Main {
    background-image: url("../images/background.png");
    background-size: cover;
  }
  .btn1 {
          position:  relative;
          width:19%;
          background-color: #f7b642;
          color:#fff;
          padding: 0.8% 0%;
          text-align: center;
          text-decoration: none;
          display: block;
          font-size: 120%;
          cursor: pointer;
          border-radius: 10px;
          letter-spacing:20px;
          left: 18%;
          top:250px;
          background-color:transparent;
          font-weight: bold;
        }
 .btn2 {
          position:  relative;
          width:19%;
          background-color: #f7b642;
          color:#fff;
          padding: 0.8% 0%;
          text-align: center;
          text-decoration: none;
          display: block;
          font-size: 120%;
          cursor: pointer;
          border-radius: 10px;
          letter-spacing:20px;
          left: 18%;
          top:280px;
          background-color:transparent;
          font-weight: bold;
        }
.subtitle{
          position:relative;
          width: 800px;
          margin: 0 auto;
          top:400px;
          left: -300px;
          text-align: center;
          font-size: 1.6em;
          color:white;
          line-height: 2em;
}
.title{
          position:relative;
          width: 800px;
          margin: 0 auto;
          top:400px;
          left: -300px;
          text-align: center;
          font-size: 2.0em;
          color:white;
          line-height: 2em;

}
 .accent {
          color:#f7b642;
        }

</style>
