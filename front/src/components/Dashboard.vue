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
          <DashboardCard  class="column is-one-quarter" v-for="sensor in sensors" :key="sensor.id" :sensor="sensor"></DashboardCard>
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
        { id: 0, topic: "home", payload: "23" },
        { id: 1, topic: "bedroom", payload: "20" },
        { id: 2, topic: "outside", payload: "19" }
      ]
      //socket: io("http://localhost:5000/")
    };
  },
  methods: {
    addCard() {
      this.sensors.push({
        id: this.sensors.length,
        topic: "new",
        payload: "NaN"
      });
    }
  },
  mounted() {
    // this.socket.on("mqtt_message", data => {
    //   this.sensors.push(data);
    // });
  }
};
</script>
