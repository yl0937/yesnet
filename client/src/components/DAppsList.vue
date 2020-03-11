<template>
<!-- 상단바 -->
  <div class="first">
          <nav aria-label="breadcrumb">
<ol class="breadcrumb" style="background-color: #f9bd5b">
	<li class="breadcrumb-item"><a href="#">DApps</a></li>
	<li class="breadcrumb-item active" aria-current="page">DApp List</li>
</ol>
</nav>

<!-- DApps / DApps List -->
<div class="shadow-sm p-3 mb-4 bg-white rounded">
	<p class="h5" style="padding-bottom: 2px; padding-top: 0;">
		<ion-icon name="list-box" class="red"></ion-icon>&nbsp; DApp List
	</p>
	 <hr color="grey" size="2px"  width="100%"/>
 	<div>
 <!-- Name / Public / UploadTime -->
	<b-table-simple hover>
    <b-thead head-variant="secondary">
      <b-tr>
        <b-th class= "Name"><strong>Name</strong></b-th>
        <b-th class= "Public"><strong>Public</strong></b-th>
        <b-th class="UploadTime"><strong>Upload Time</strong></b-th>
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
</div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'first',
  data() {
    isShowing:false
    return {
        fields: [
          'name',
          'public',
          'upload_time',
          'deployment'
        ],
        items: []
    }
  },
  methods:{
  getJSONResponse () {
    const token = sessionStorage.getItem("access_token")
        //console.log(token)
    const path = 'http://localhost:9999/api/show_dapp'
    axios
    .get(path, { params: {},
        headers: {
            "Authorization": token
        }
    })
    .then(response => {
       this.items = response.data.payload
    })
    .catch(error => {
        // eslint-disable-next-line no-console
        console.log(error)
    })
  },
    DeploymentDApps(app_id){
    const token = sessionStorage.getItem("access_token")
    axios.post('http://localhost:9999/api/deploymentPost',
        {dapp_id:app_id},
        {headers: {
            "Authorization": token
           }
        })
    .then(response => {
        let code
        let err_name
        let reason
        code = response.data.code
        err_name = response.data.err_name
        reason = response.data.reason

       if(code == '200'){
        alert('Success')
       }
       if(code != '200'){
        alert('Fail'+err_name+reason)
       }
    })
    .catch(error => {
        console.log(error)
    })
    },
    date: function (date) {
      return moment(date).format('YYYY/MM/DD h:mm a');
    }

},
    created () {
        this.getJSONResponse()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.h3 {
  margin: 40px 0 0;
}
.ul {
  list-style-type: none;
  padding: 0;
}
.li {
  display: inline-block;
  margin: 0 10px;
  padding-top: 0;
}
.a {
  color: black;
}
.h5 {
  margin: 0;
  font-size: 1.5em;
  text-align: left;
  weight:100px;
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
</style>
