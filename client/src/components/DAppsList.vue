<template>
  <div class="first">
          <nav aria-label="breadcrumb">
<ol class="breadcrumb" style="background-color: #2e2e2e">
 <li class="breadcrumb-item"><a href="#">DApps</a></li>
 <li class="breadcrumb-item active" aria-current="page">DApp List</li>
</ol>
</nav>

<div class="shadow-sm p-3 mb-4 bg-white rounded">
 <p class="h5" style="padding-bottom: 50px; padding-top:80px;">
  <ion-icon name="list-box" class="red"></ion-icon>&nbsp; DApp List
 </p>
  <b-table-simple hover>
    <b-thead head-variant="secondary">
      <b-tr>
        <b-th>Name</b-th>
        <b-th>Public</b-th>
        <b-th>Upload Time</b-th>
        <b-th> </b-th>
      </b-tr>
    </b-thead>
    <b-tbody>
      <b-tr v-for="item in items">
        <b-td>{{item.name}}</b-td>
        <b-td>{{item.public}}</b-td>
        <b-td>{{date(item.upload_time.$date)}}</b-td>
        <b-td><b-button @click="DeploymentDApps(item._id)">Deployment</b-button></b-td>
      </b-tr>
    </b-tbody>
  </b-table-simple>
</div>
</div>
</template>

<script>
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
