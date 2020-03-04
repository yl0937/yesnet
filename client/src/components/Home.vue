<template>
<!-- 상단바 -->
<div>
      <nav aria-label="breadcrumb">
<ol class="breadcrumb" style="background-color: #f9bd5b">
	<li class="breadcrumb-item"><a href="#">Home</a></li>
	<li class="breadcrumb-item active" aria-current="page">Dashboard</li>
</ol>
</nav>

<!-- ETH content -->
<div class="shadow-sm p-3 mb-4 bg-white rounded">
	<p class="ETH content" style="" size="sm">
    <ethmodal />
	</p>
</div>

<!-- View DApps content-->
<div class="shadow-sm p-3 mb-4bg-white rounded">
	<p class="h5" style="padding-bottom: 2px; padding-top: 0;">
		<ion-icon name="list-box" class="red"></ion-icon>&nbsp; View DApps
	</p>
   <hr color="grey" size="2px"  width="100%"/>

<!-- Name, Public, Upload -->
	<div>
	<b-table-simple hover>
    <b-thead head-variant="secondary">
      <b-tr>
        <b-th class= "Name"><strong>Name</strong></b-th>
        <b-th class= "Public"><strong>Public</strong></b-th>
        <b-th class="UploadTime"><strong>Upload Time</strong></b-th>
      </b-tr>
    </b-thead>
<!-- 작동 안되는거같음 -->
    <b-tbody>
      <b-tr v-for="item in items">
        <b-td>{{item.name}}</b-td>
        <b-td>{{item.public}}</b-td>
        <b-td>{{date(item.upload_time.$date)}}</b-td>
      </b-tr>
    </b-tbody>
  </b-table-simple>
</div>
</div>
</div>
</template>


<style scoped>
.a{
color: black;
}
.ETH content{
  margin: 0;
  font-size: 1.5em;
  text-align: left;
}
.h5 {
  margin: 0;
  font-size: 1.5em;
  text-align: left;
  weight:100px;
}
.ul,ol {
  padding-left: 10px;
}
.Name{
  width: 70px;
  float: left;
  font-size: 1.1em;
}
.Public{
 width: 1000px;
  float: left;
  font-size: 1.1em;
}
.UploadTime{
 width:500px;
  float: left;
  font-size: 1.1em;
}
 .hr{
 position: absolute;
        left: 700px;
        top: 50px;
 }
</style>
