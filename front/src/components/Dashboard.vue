<template>
  <div>
    <section class="hero is-light">
      <div class="hero-head">
        <nav class="navbar">
          <div class="container">
            <div id="navbarMenuHeroA" class="navbar-menu">
              <div class="navbar-start">
                <span class="navbar-item">
                  <h1 class="title">MQTT Dashboard</h1>
                </span>
              </div>
              <div class="navbar-end">
                <span class="navbar-item">
                  <a class="icon is-large has-text-dark">
                    <i class="mdi mdi-36px mdi-plus-box" @click="addCard"></i>
                  </a>
                </span>
              </div>
            </div>
          </div>
        </nav>
      </div>
    </section>
    <br />
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-one-quarter" v-for="device in devices" :key="device.id">
          <DashboardCard :device="device" @delete-card="deleteCard"></DashboardCard>
        </div>
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
      devices: [
        { id: 0, topic: "home/kitchen", payload: "23", type: "Sensor" },
        { id: 1, topic: "home/bedroom", payload: "20", type: "Sensor" },
        { id: 2, topic: "home/outside", payload: "19", type: "Sensor" }
      ]
      //socket: io("http://localhost:5000/")
    };
  },
  methods: {
    addCard() {
      this.devices.push({
        id: this.devices[this.devices.length - 1].id + 1,
        topic: "new",
        payload: "NaN",
        type: "Sensor"
      });
    },
    deleteCard(id) {
      let index = this.devices.findIndex(x => x.id === id)
      this.devices.splice(index, 1);
    }
  },
  mounted() {
    // this.socket.on("mqtt_message", data => {
    //   this.sensors.push(data);
    // });
  }
};
</script>
