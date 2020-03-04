<template>
<!-- 내부 상단바 -->
  <div class="first">
          <nav aria-label="breadcrumb">
<ol class="breadcrumb" style="background-color: #f9bd5b">
    <li class="breadcrumb-item"><a href="#">DApps</a></li>
    <li class="breadcrumb-item active" aria-current="page">Deployed DApp</li>
</ol>
</nav>

<!-- DApps/Deployed DApp-->
<div class="shadow-sm p-3 mb-4 bg-white rounded">
    <p class="h5" style="padding-bottom: 8px; padding-top:7px;">
        <ion-icon name="list-box" class="red"></ion-icon>  Deployed DApp
    </p>
  <div>
  <b-table hover :items="items1" :fields="fields">
      <template v-slot:function="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show'}} Details
        </b-button>
      </template>

      <template v-slot:row-details="row">
        <b-card>
        <div>
  <b-table-simple hover>
    <b-thead>
      <b-tr variant="secondary">
        <b-td>Name</b-td>
        <b-td>Inputs</b-td>
        <b-td> </b-td>
      </b-tr>
    </b-thead>
    <b-tbody>
      <b-tr v-for="(item, index) in functionList">
        <b-td>{{item.name}}</b-td>
        <b-td>{{item.inputs}}</b-td>
        <b-td><div v-if="calltxcheck[index]==='A'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('modal-prevent-closing2');functionEx(index)">Launch</b-button></div>
              <div v-else-if="calltxcheck[index]==='B'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('alertmodal');functionEx(index)">Launch</b-button></div>
              <div v-else-if="calltxcheck[index]==='C'"><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('modal-prevent-closing');functionEx(index)">Launch</b-button></div>
              <div v-else><b-button v-b-toggle="'collapse-2'" class="sm" size="sm" @click="$bvModal.show('txalertmodal');functionEx(index)">Launch</b-button></div>
          </b-td>
      </b-tr>
    </b-tbody>
  </b-table-simple>
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
</script>

<style scoped>
.a {
  color:black;
}

.h5 {
  margin: 15px;
  font-size: 1.5em;
  text-align: left;
  weight:100px;

}
</style>
