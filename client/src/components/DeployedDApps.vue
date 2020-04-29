<template>
  <div class="first">

<div class="shadow-sm p-3 mb-4 ">
    <p class="h5" style="padding-bottom: 8px; padding-top:7px;">
        <ion-icon name="list-box" class="red"></ion-icon>  Deployed DApp
    </p>
  <div>
    <b-table :items="items1" :fields="fields" striped responsive="sm">
      <template v-slot:cell(function)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Details
        </b-button>

        <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->

      </template>

      <template v-slot:row-details="row">
        <b-card>
           <div>
             <b-table :items="items2" :fields="fields2" striped responsive="sm">
               <template v-slot:cell(function)="row"></template>
             </b-table>
           </div>
        </b-card>
        <b-card>
          <div>
          <b-table-simple hover>
          <b-thead>
            <b-tr variant="secondary">
              <b-td>Type</b-td>
              <b-td>Name</b-td>
              <b-td>Inputs</b-td>
              <b-td> </b-td>
             </b-tr>
          </b-thead>
          <b-tbody>
              <b-tr v-for="(item, index) in functionList">
              <b-td>
                  <div v-if="calltxcheck[index]==='A'">Call(params O)</div>
                  <div v-else-if="calltxcheck[index]==='B'">Call(params X)</div>
                  <div v-else-if="calltxcheck[index]==='C'">Tx(params O)</div>
                  <div v-else>Tx(params X)</div>
                </b-td>
                <b-td>{{item.name}}</b-td>
              <b-td>{{item.inputs}}</b-td>
              <b-td><div v-if="calltxcheck[index]==='A'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('modal-prevent-closing2');functionEx(index)">LaunchA</b-button></div>
              <div v-else-if="calltxcheck[index]==='B'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('alertmodal');functionEx(index)">LaunchB</b-button></div>
              <div v-else-if="calltxcheck[index]==='C'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('modal-prevent-closing');functionEx(index)">LaunchC</b-button></div>
              <div v-else><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('txalertmodal');functionEx(index)">LaunchD</b-button></div>
              <b-td><div v-if="calltxcheck[index]==='A'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('modal-prevent-closing2');functionEx(index)">Launch</b-button></div>
              <div v-else-if="calltxcheck[index]==='B'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('alertmodal');functionEx(index)">Launch</b-button></div>
              <div v-else-if="calltxcheck[index]==='C'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('modal-prevent-closing');functionEx(index)">Launch</b-button></div>
              <div v-else><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('txalertmodal');functionEx(index)">Launch</b-button></div>
              </b-td>
              </b-td>
              </b-tr>
          </b-tbody>
          </b-table-simple>
            <b-button size="sm" @click="row.toggleDetails">Hide Details</b-button>
              </div>
        </b-card>
      </template>
    </b-table>
  </div>
  <div>
    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Submit Parameter"
      @show="resetModal"
      @hidden="resetModal"
      @ok="txhandleOk"
    >
     <div>
      <form ref="form" @submit.stop.prevent="txhandleSubmit">
        <ul>
        <li v-for="(method, index) in functionNames">
        <p>{{method}} Parameter</p>

        <b-form-group
          :state="nameState"
          label-for="param-input"
          valid-feedback="Param is required"
        >
          <b-form-input
            id="name-input"
            v-model="name[index]"
            :state="nameState"
          ></b-form-input>
        </b-form-group>
        </li>
        </ul>
      </form>
     </div>
      <p>Do you want to launch the function?</p>
    </b-modal>


    <b-modal
      id="modal-prevent-closing2"
      ref="modal"
      title="Submit Parameter"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
     <div>
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <ul>
        <li v-for="(param, index) in functionNames">
        <p>{{param}} Parameter</p>

        <b-form-group
          :state="modalState"
          label-for="param-input"
          valid-feedback="Param is required"
        >
          <b-form-input
            id="name-input"
            v-model="paramArr[index]"
            :state="modalState"
          ></b-form-input>
        </b-form-group>
        </li>
        </ul>
      </form>
     </div>
      <p>Do you want to launch the function?</p>
    </b-modal>

      <b-modal id="alertmodal" title="Launch Function(Call)" @ok="alerthandleok">
        <p class="my-4">Do you want to launch the function?</p>
      </b-modal>

      <b-modal id="txalertmodal" title="Launch Function(Tx)" @ok="txalerthandleok">
        <p class="my-4">Do you want to launch the function?</p>
      </b-modal>

</div>
</div>
  </div>
</template>

<script>
//import abi from './abi.vue';
import axios from 'axios'
import moment from 'moment'

export default {
    name: 'first',
    data() {
        return {
            fields: ['timestamp', 'gasUsed', 'contractAddress', 'function'],
            fields2:[],
            items1: [],
            items2:[],
            functionList: [],
            method: null,
            name: [],
            nameState: null,
            submittedNames: [],
            param: null,
            functionNames: [],
            modalState: null,
            isShowing: false,
            calltxcheck: [],
            paramArr: [],
            functionNames2: [],
            name2: [],
            submittedParam: [],
            paramState: [],
            abi: null,
            arraydata: {},
            dictObject: []
        }
    },
    methods: {
        functionEx(index) {
            this.arraydata.functionName = this.functionList[index].name

            this.functionNames.splice(0)
            for (var input of this.functionList[index].inputs) {
                this.functionNames.push(input.name)
            }
        },
        getJSONResponse() {
            const token = sessionStorage.getItem("access_token")
            //console.log(token)
            const path = 'http://localhost:9999/api/getDApp'
            axios
                .get(path, {
                    params: {},
                    headers: {
                        "Authorization": token
                    }
                })
                .then(response => {
                    for (var arr of response.data.payload) {
                        //console.log(arr.timestamp)
                        let time = arr.timestamp
                        //console.log(time)
                        let changetime = moment.unix(time).format('YYYY/MM/DD h:mm:ss a');
                        //console.log(changetime)
                        arr.timestamp = changetime

                        let abi = arr.abi
                        this.abi = abi

                        this.calltxcheck.splice(0)
                        for (var x of arr.funtions) {
                            //console.log(x.name, typeof(x.constant), x.constant, x)
                            this.dictObject = x.inputs
                            var cons = Boolean(x.constant)

                            if (cons) {
                                //console.log(x.name, x.constant)
                                if (this.dictObject.length > 0) {
                                    this.calltxcheck.push('A')
                                } else {
                                    this.calltxcheck.push('B')
                                }

                            } else {
                                if (this.dictObject.length > 0) {
                                    this.calltxcheck.push('C')
                                } else {
                                    this.calltxcheck.push('D')
                                }
                            }
                            this.functionList = arr.funtions

                        }
                    }
                    this.items1 = response.data.payload
                    console.log(this.items2)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })
        },
        checkFormValidity() {
            const valid = this.$refs.form.checkValidity()
            this.nameState = valid ? 'valid' : 'invalid'
            return valid
        },
        resetModal() {
            this.name = []
            this.nameState = null
            this.paramArr = []
            this.modalState = null
        },
        handleOk(bvModalEvt) {
            // Prevent modal from closing
            bvModalEvt.preventDefault()
            // Trigger submit handler
            this.handleSubmit()
            this.argsPost()
        },
        handleSubmit() {
            // Exit when the form isn't valid
            if (!this.checkFormValidity()) {
                return
            }
            // Push the name to submitted names
            this.submittedNames.push(this.name)
            // Hide the modal manually
            this.$nextTick(() => {
                this.$refs.modal.hide()
            })
        },
        argsPost() {
            let args = {}

            //let args_name
            let args_names = []
            let args_vals = []

            args_names = this.functionNames

            let paramintArr = []
            for (var inte of this.paramArr) {
                inte = parseInt(inte)
                paramintArr.push(inte)
            }
            args_vals = paramintArr
            for (var a in args_names) {
                args[args_names[a]] = args_vals[a]
            }
            //args[args_name] = args_val
            for (var i of this.items1) {
                this.arraydata.contractAddress = i.contractAddress
            }
            this.arraydata.abi = this.abi
            this.arraydata.args = args
            // eslint-disable-next-line no-console
            console.log('arraydata :', this.arraydata)
            axios.post('http://localhost:9999/api/callFunction',
                this.arraydata
            )
            // eslint-disable-next-line no-unused-vars
                .then(response => {
                    let str = JSON.stringify(response.data.result.return)
                    alert(str)
                    console.log(response)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })
        },
        txhandleOk(bvModalEvt) {
            // Prevent modal from closing
            bvModalEvt.preventDefault()
            // Trigger submit handler
            this.txhandleSubmit()
            this.txargsPost()
        },
        txhandleSubmit() {
            // Exit when the form isn't valid
            if (!this.checkFormValidity()) {
                return
            }
            // Push the name to submitted names
            this.submittedNames.push(this.name)
            // Hide the modal manually
            this.$nextTick(() => {
                this.$refs.modal.hide()
            })
        },
        txargsPost() {
            let args = {}

            //let args_name
            //let args_val
            let args_names = []
            let args_vals = []

            args_names = this.functionNames
            args_vals = this.name
            for (var a in args_names) {
                args[args_names[a]] = args_vals[a]
            }
            //args[args_name] = args_val
            for (var i of this.items1) {
                this.arraydata.contractAddress = i.contractAddress
            }
            this.arraydata.abi = this.abi
            this.arraydata.args = args
            // eslint-disable-next-line no-console
            console.log('arraydata :', this.arraydata)
            axios.post('http://localhost:9999/api/callTx',
                this.arraydata
            )
            // eslint-disable-next-line no-unused-vars
                .then(response => {
                    let str = JSON.stringify(response.data.result.return)
                    alert(str)
                    console.log(response)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })
        },
        noargsPost() {
            for (var i of this.items1) {
                this.arraydata.contractAddress = i.contractAddress
            }
            this.arraydata.abi = this.abi
            this.$delete(this.arraydata, 'args')
            // eslint-disable-next-line no-console
            console.log('arraydata :', this.arraydata)
            axios.post('http://localhost:9999/api/callFunction',
                this.arraydata
            )
                .then(response => {
                    let str = JSON.stringify(response.data.result.return)
                    alert(str)
                    console.log(response)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })

        },
        notxargsPost() {
            for (var i of this.items1) {
                this.arraydata.contractAddress = i.contractAddress
            }
            this.arraydata.abi = this.abi
            this.$delete(this.arraydata, 'args')
            // eslint-disable-next-line no-console
            console.log('arraydata :', this.arraydata)
            axios.post('http://localhost:9999/api/callTx',
                this.arraydata
            )
                .then(response => {
                    let str = JSON.stringify(response.data.result.return)
                    alert(str)
                    console.log(response)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })

        },
        alerthandleok() {
            this.noargsPost()
                .then(response => {
                    // eslint-disable-next-line no-console
                    console.log(response.result)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })
        },
        txalerthandleok() {
            this.notxargsPost()
                .then(response => {
                    // eslint-disable-next-line no-console
                    console.log(response.result)
                })
                .catch(error => {
                    // eslint-disable-next-line no-console
                    console.log(error)
                })
        }
    },
    created() {
        this.getJSONResponse()
    },
}

</script>
