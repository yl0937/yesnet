<template>
<div class="input-group mb-3">
    <div class="input-group-prepend">
        <button class="btn btn-outline-secondary" type="button" id="inputGroupFileAddon03">Abi</button>
    </div>
    <b-form-file v-model="file" @change="loadTextFromFile"></b-form-file>
  </div>
</template>

<script>
export default {
  methods: {
    loadTextFromFile(ev) {
      const file = ev.target.files[0];
      const reader = new FileReader();

      reader.onload = e => this.$emit("load", e.target.result);
      reader.readAsText(file);
    }
  }
};
</script>