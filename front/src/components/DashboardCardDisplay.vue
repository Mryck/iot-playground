<template>
  <div>
    <article key="1" class="media">
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
  </div>
</template>

<script>
import "@mdi/font/css/materialdesignicons.css";

export default {
  props: {
    device: Object
  },
  // data() {},
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
    }
  }
};
</script>
