<template>
  <div>
    <div class="columns is-multiline">
      <div class="column is-one-quarter" v-for="sensor in sensors" :key="sensor.topic">
        <DashboardCard :topic="sensor.topic" :payload="sensor.payload"></DashboardCard>
      </div>
    </div>
  </div>
</template>

<script>
//import io from "socket.io-client";
import DashboardCard from "./DashboardCard.vue";

export default {
  components: {
    DashboardCard
  },
  data() {
    return {
      sensors: [
        { topic: "home", payload: "23" },
        { topic: "bedroom", payload: "20" },
        { topic: "outside", payload: "19" }
      ]
      //socket: io("http://localhost:5000/")
    };
  },
  mounted() {
    // this.socket.on("mqtt_message", data => {
    //   this.sensors.push(data);
    // });
  }
};
</script>
