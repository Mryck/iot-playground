<template>
  <div>
    <div class="box">
      <transition name="fade" mode="out-in">
        <article key="1" v-if="!isSettingsVisible" class="media">
          <div class="media-content">
            <p class="title is-5">{{ sensor.topic }}</p>
            <p class="is-size-1 has-text-centered">{{ sensor.payload }}</p>
          </div>
          <a class="has-text-right">
            <span class="icon has-text-info is-medium has-text-right">
              <i class="mdi mdi-24px mdi-settings" @click="showSettings"></i>
            </span>
          </a>
        </article>
        <article key="2" v-else class="media">
          <div class="media-content">
            <p class="title is-5">Settings</p>
            <input v-model="sensor.topic" />
          </div>
          <a class="has-text-right">
            <span class="icon has-text-info is-medium has-text-right">
              <i class="mdi mdi-24px mdi-close" @click="closeSettings"></i>
            </span>
          </a>
        </article>
      </transition>
    </div>
  </div>
</template>

<script>
//import io from "socket.io-client";
import "@mdi/font/css/materialdesignicons.css";

export default {
  props: {
    sensor: Object
  },
  data() {
    return {
      isSettingsVisible: false
      // sensors: [
      //   { topic: "home", payload: "23" },
      //   { topic: "bedroom", payload: "20" },
      //   { topic: "outside", payload: "19" }
      // ]
      // //socket: io("http://localhost:5000/")
    };
  },
  methods: {
    showSettings() {
      this.isSettingsVisible = true;
    },
    closeSettings() {
      this.isSettingsVisible = false;
    }
  },
  mounted() {
    // this.socket.on("mqtt_message", data => {
    //   this.sensors.push(data);
    // });
  }
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>