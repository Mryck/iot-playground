<template>
  <div>
    <article key="1" class="media">
      <div class="media-content">
        <p class="title is-5">
          <span class="icon has-text-dark">
            <i v-if="device.type == 'Sensor'" class="mdi mdi-24px mdi-thermometer"></i>
            <i v-else class="mdi mdi-24px mdi-lightbulb"></i>
          </span>
          {{ deviceName }}
        </p>
        <p v-if="device.type == 'Sensor'" class="is-size-1 has-text-centered">{{ device.payload }}</p>
        <p v-else class="is-size-1 has-text-centered">
          <a v-show="this.switchState" class="icon is-large has-text-warning">
            <i class="mdi mdi-48px mdi-toggle-switch" @click="toggle"></i>
          </a>
          <a v-show="!this.switchState" class="icon is-large has-text-dark">
            <i class="mdi mdi-48px mdi-toggle-switch-off" @click="toggle"></i>
          </a>
        </p>
      </div>
      <a class="has-text-right">
        <span class="icon has-text-info is-medium has-text-right">
          <i class="mdi mdi-24px mdi-settings" @click="showSettings"></i>
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
  data() {
    return {
      switchState: false
    };
  },
  computed: {
    deviceName: function() {
      // Return the name of the device from the topic (home/sensor/kitchen = kitchen)
      return this.device.topic.split("/")[
        this.device.topic.split("/").length - 1
      ];
    }
  },
  methods: {
    showSettings() {
      this.$emit("toggle-settings", true);
    },
    toggle() {
      this.switchState = !this.switchState;
    }
  }
};
</script>
