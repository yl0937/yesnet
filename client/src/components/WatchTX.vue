<template>
  <div>
<div class="shadow-sm p-3 mb-4 bg-white rounded">
	<p class="h5" style="padding-bottom: 8px; padding-top:7px;">
		<ion-icon name="list-box" class="yellow"></ion-icon>&nbsp;Watch TX
	</p>
<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Write down the TxHash" aria-label="Receipient's usernam" aria-describedby="basic-addon2" v-model="txHash">
  <div class="input-group-append">
    <button class="btn btn-dark" type="button" @click="getJSONResponse">Show</button>
  </div>

</div>

<json-viewer
    :value="axiosjsonData"
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
          axiosjsonData:'value is Empty',
          txHash:''
      }

},
    components: {
    JsonViewer
    },
  methods:{
  getJSONResponse () {
      const token = sessionStorage.getItem("access_token")
      const path = 'http://localhost:9999/api/watchtx'

      axios
        .post(path,
            {txHash: this.txHash},
            {
            headers: {
                "Authorization": token
            },
        })

        .then(response => {
            let txInfo = response
            delete(txInfo.data.txInfo.input)

            this.axiosjsonData=txInfo
        // let code = response.data.result.code
        // let err_name = response.data.result.err_name
        // let reason = response.data.result.reason


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
</style>
