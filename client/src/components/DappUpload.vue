<template>

    <div>
    <!-- DApp Deployment -->
    <div class="shadow-sm p-3 mb-4">
        <p class="h5" style="padding-bottom: 8px; padding-top:0px; ">
            DApp Deployment
        </p>
      <hr color="grey" size="2px"  width="100%"/>

    <!-- DApps Name/ Description -->
    <div class="input-group mb-3">
    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <button class="btn btn-outline-secondary" type="button" id="button-addon1">DApps Name</button>
      </div>
      <input type="text" class="form-control" v-model="name" aria-label="Example text with button addon" aria-describedby="button-addon1">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <button class="btn btn-outline-secondary" type="button" id="button-addon2">Description</button>
      </div>
      <input type="text" class="form-control" v-model="desc" aria-label="Example text with button addon" aria-describedby="button-addon2">
    </div>

        <text-reader @load="text = $event"></text-reader>
    <json-viewer
        v-model="text"
        :expand-depth=5
        boxed
        sort></json-viewer>
        <br/>

        <bin-reader @load="text2 = $event"></bin-reader>
    <json-viewer
        v-model="text2"
        :expand-depth=5
        boxed
        sort></json-viewer>
        <br/>
      </div>


    <!-- 버튼 -->

    <p style= "text-align:left;">
    <button type="button" class="btn btn-warning" @click="addDApp">Upload</button>
    <button type="button" class="btn btn-dark" @click="resetForm">Reset</button>
    </p>
    </div>




    </div>
</template>

<script>
import axios from 'axios'
import JsonViewer from 'vue-json-viewer'
import TextReader from './src/TextReader'
import BinReader from './src/BinReader'

export default {
 data() {
      return {
        form: {
          checked: []
        },
        show: true,
        text: '',
        text2: ''
      }
    },
    components: {
     TextReader,
     BinReader,
    JsonViewer
    },
      methods: {
        resetForm(){
            this.text=""
            this.text2=""
            this.name=""
            this.desc=""
        },
        formatNames(files) {
        if (files.length === 1) {
          return files[0].name
        } else {
          return `${files.length} files selected`
        }
      },
       addDApp(){
          const token = sessionStorage.getItem("access_token")
          this.text2=this.text2.replace(/(\n)/gm,"")

          axios.post('http://localhost:9999/api/add_dapp',
            {name:this.name, desc:this.desc, abi:this.text, bin:this.text2},
                {
                headers: {
                    "Authorization": token
                }
              }
        ).then(response => {
            this.result = response.data
            alert('success')
        }).catch((ex) => {
              // eslint-disable-next-line no-console
            console.warn("ERROR : ", ex)
            alert("ERROR : ", ex)
        })
      }
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 500px;
}
h5{
  margin: 15px;
  font-size: 1.5em;
  text-align: left;
  weight:100px;

}
ul{
  list-style-type: none;
  padding: 0;
}
li{
  margin: 0 10px;

}
a{
  color: black;
}

</style>
