<template>
  <div>
    <div class="box">
      <transition name="fade" mode="out-in">
        <article key="1" v-if="!isSettingsVisible" class="media">
          <div class="media-content">
            <p class="title is-5">
              <span class="icon has-text-dark">
                <i v-if="device.type == 'Sensor'" class="mdi mdi-24px mdi-thermometer"></i>
                <i v-else class="mdi mdi-24px mdi-toggle-switch"></i>
              </span>
              {{ deviceName }}
            </p>
            <p class="is-size-1 has-text-centered">{{ device.payload }}</p>
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
      </transition>
    </div>
  </div>
</template>

<script>
//import io from "socket.io-client";
import "@mdi/font/css/materialdesignicons.css";

export default {
  props: {
    device: Object
  },
  data() {
    return {
      isSettingsVisible: false,
      deviceType: "Sensor"
      // sensors: [
      //   { topic: "home", payload: "23" },
      //   { topic: "bedroom", payload: "20" },
      //   { topic: "outside", payload: "19" }
      // ]
      // //socket: io("http://localhost:5000/")
    };
  },
  computed: {
    deviceName: function() {
      return this.device.topic.split("/")[
        this.device.topic.split("/").length - 1
      ];
    }
  },
  methods: {
    deleteCard() {
      this.$emit("delete-card", this.device.id);
    },
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