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
    };
  },
  methods: {
    addCard() {
      let newIndex;
      if (this.devices.length === 0) {
        newIndex = 0;
      } else {
        newIndex = this.devices[this.devices.length - 1].id + 1;
      }
      this.devices.push({
        id: newIndex,
        topic: "new",
        payload: "NaN",
        type: "Sensor"
      });
    },
    deleteCard(id) {
      let index = this.devices.findIndex(x => x.id === id);
      this.devices.splice(index, 1);
    }
  },
  // Specific integration to handle incomming socketio message from the backend
  sockets: {
    mqtt_message(data) {
      let index = this.devices.findIndex(x => x.topic === data.topic);
      this.devices[index].payload = data.payload;
    }
  },
  mounted() {
    // On mounted, subscribe to all known devices, later fetch from tinyDB
    var topic = "home/kitchen";
    var qos = 0;
    var data = { topic: topic, qos: qos };
    this.$socket.emit("subscribe", JSON.stringify(data));
  },
  beforeDestroy() {
    // for now unsubscribe to all topic on Destroy
    this.$socket.emit("unsubscribe_all");
  }
};
</script>
