<template>
  <div>
    <div class="box">
      <transition name="fade" mode="out-in">
        <!-- main display of the card with value -->
        <DashboardCardDisplay
          v-if="!isSettingsVisible"
          :device="device"
          @toggle-settings="toggleSettings"
        ></DashboardCardDisplay>
        <!-- settings diplay of the card -->
        <DashboardCardSettings
          v-else
          :device="device"
          @delete-card="deleteCard"
          @toggle-settings="toggleSettings"
        ></DashboardCardSettings>
      </transition>
    </div>
  </div>
</template>

<script>
import DashboardCardDisplay from "./DashboardCardDisplay";
import DashboardCardSettings from "./DashboardCardSettings";

import "@mdi/font/css/materialdesignicons.css";

export default {
  components: {
    DashboardCardDisplay,
    DashboardCardSettings
  },
  props: {
    device: Object
  },
  data() {
    return {
      isSettingsVisible: false
    };
  },
  methods: {
    deleteCard() {
      this.$emit("delete-card", this.device.id);
    },
    toggleSettings(state) {
      this.isSettingsVisible = state;
    }
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