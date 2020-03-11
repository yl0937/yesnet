<template>
  <div>
    <div class="mb-2">
      <p class="h5">
      <b-badge variant="warning">ETH</b-badge>
        Your Ethereum Balance: {{balance}} Wei
       <b-button v-b-modal.modal-1 class="btn-dark" size="sm">Charging Ethereum</b-button>
       <b-modal id="modal-1" title="Charging Ethereum">
         Charging 100 Ethereum
         <template slot="modal-footer" slot-scope="{ ok, cancel}">
      <b-button size="sm" variant="dark" @click="showMsgBoxOne(), ok()">
        OK
      </b-button>
      <b-button size="sm" @click="cancel()">
        Cancel
      </b-button>
    </template>
         </b-modal>
         </p>
        </div>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
      return {
          balance: 0
      }
    },
    methods: {
      showMsgBoxOne() {
        const token = sessionStorage.getItem("access_token")
        const path = 'http://localhost:9999/api/fill_eth'

        axios
        .get(path, { params: {},
            headers: {
                "Authorization": token
            },
        })
        .then(response => {
           this.balance = response.data.result.balance
        })
        .catch(error => {
            console.log(error)
        })
      },
    getJSONResponse () {
        const token = sessionStorage.getItem("access_token")
        const path = 'http://localhost:9999/api/balance'

        axios
        .get(path, { params: {},
            headers: {
                "Authorization": token
            },
        })
        .then(response => {
           this.balance = response.data.result.balance
        })
        .catch(error => {
            // eslint-disable-next-line no-console
            console.log(error)
        })
  }

  },
  created () {
        this.getJSONResponse()
    }

    }
</script>
