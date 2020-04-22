<template>
  <div>
<div class="shadow-sm p-3 mb-4">
	<p class="h5" style="padding-bottom: 8px; padding-top:0px;">
		<ion-icon name="list-box" class="yellow"></ion-icon>&nbsp;Watch Block
	</p>
    <hr color="grey" size="2px"  width="100%"/>
<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Write down the Block Number" aria-label="Receipient's usernam" aria-describedby="basic-addon2" v-model="blockNum">
  <div class="input-group-append">
    <button class="btn btn-dark" type="button" @click="getJSONResponse">Search</button>
  </div>
</div>

<json-viewer

    :expand-depth=5
    copyable
    boxed
    sort></json-viewer>

</div>
  </div>
</template>

<script>
import axios from 'axios'
import JsonViewer from 'vue-json-viewer'

  export default {
    data() {
      return {
          token:null,
          blockNum: ''
      }
},
    components: {
    JsonViewer
    },
  methods:{
  getJSONResponse () {
        const token = sessionStorage.getItem("access_token")
        //const path = '/api/watchblock'

      this.blockNum = parseInt(this.blockNum)

    axios
    .post('http://localhost:9999/api/watchblock',
        {'blockNum':this.blockNum},
        {
        headers: {
            "Authorization": token
        }
    },
)
    .then(response => {
        let code=response.data.result.code
        let err_name=response.data.result.err_name
        let reason=response.data.result.reason

       this.axiosjsonData = response.data.result.blockInfo
        if(code != 200){
            alert(err_name+reason)
        }
    })
    .catch(error => {
        console.log(error)
    })
  }

}
  }
</script>
<style>
                body { padding:0px;
                background-color: #f1f2f7;
                }
                .yellow {color:#f2b441;}
                .grey {color: #5d667b;}
                a:link {color:#f2b441;}
                .jbGrad02 {background: linear-gradient( to top, white, #e5ffac );}
                .jbGrad03 {background: linear-gradient( to top, white, #d7d7d7 );}
                .jbGrad04 {background: linear-gradient( to top, white, #ade9f7 );}
.h5 {
  margin: 15px;
  font-size: 1.5em;
  text-align: left;
  weight:100px;
}
</style>
