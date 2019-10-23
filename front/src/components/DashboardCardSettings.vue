<template>
  <div>
    <article key="2" class="media">
      <div class="media-content">
        <p class="title is-5">Settings</p>
        <p>
          mqtt topic:
          <input v-model="device.topic" />
        </p>
        <br />
        <p>Device type:</p>
        <div class="control">
          <label class="radio">
            <input type="radio" v-model="device.type" value="Sensor" />
            Sensor
          </label>
          <label class="radio">
            <input type="radio" v-model="device.type" value="Switch" />
            Switch
          </label>
        </div>
        <p class="has-text-right">
          <a>
            <span class="icon has-text-danger is-medium has-text-right">
              <i class="mdi mdi-24px mdi-delete" @click="deleteCard"></i>
            </span>
          </a>
        </p>
      </div>
      <a class="has-text-right">
        <span class="icon has-text-info is-medium has-text-right">
          <i class="mdi mdi-24px mdi-close" @click="closeSettings"></i>
        </span>
      </a>
    </article>
  </div>
</template>

<script>
import "@mdi/font/css/materialdesignicons.css";

export default {
  props: {
    device: Object
  },
  // data() {},
  methods: {
    deleteCard() {
      this.$emit("delete-card", this.device.id);
    },
    closeSettings() {
      this.$emit("toggle-settings", false);
    }
  }
};
</script>