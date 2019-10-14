<template>
  <div>
    <div class="columns is-multiline">
      <div class="column is-one-quarter" v-for="sensor in sensors" :key="sensor.topic">
        <div class="box">
          <article class="media">
            <div class="media-content">
              <p class="title is-5">{{ sensor.topic }}</p>
              <p class="is-size-1 has-text-centered">{{ sensor.payload }}</p>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import io from "socket.io-client";

export default {
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
