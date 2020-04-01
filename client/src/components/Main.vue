<template>
  <div class="admin-container2">
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
</template>

<script>
    export default {
        name: "Main"
    }
</script>

<style scoped>
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
          left: 40%;
          top:370px;
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
          left: 40%;
          top:395px;
          background-color:transparent;
          font-weight: bold;
        }
.subtitle{
          position:relative;
          width: 800px;
          margin: 0 auto;
          top:500px;
          left: -5px;
          text-align: center;
          font-size: 1.6em;
          color:white;
          line-height: 2em;
}
.title{
          position:relative;
          width: 800px;
          margin: 0 auto;
          top:510px;
          left: -10px;
          text-align: center;
          font-size: 2.0em;
          color:white;
          line-height: 2em;

}
 .accent {
          color:#f7b642;
        }

</style>
