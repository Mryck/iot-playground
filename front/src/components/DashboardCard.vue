<template>
  <div>
    <div class="box">
      <article class="media">
        <div class="media-content">
          <p class="title is-5">{{ topic }}</p>
          <p class="is-size-1 has-text-centered">{{ payload }}</p>
        </div>
        <a class="has-text-right">
          <span class="icon has-text-info is-medium has-text-right">
            <i class="mdi mdi-24px mdi-settings"></i>
          </span>
        </a>
      </article>
    </div>
  </div>
</template>

<script>
//import io from "socket.io-client";
import "@mdi/font/css/materialdesignicons.css";

export default {
  props: {
    topic: String,
    payload: String
  },
  data() {
    return {
      // sensors: [
      //   { topic: "home", payload: "23" },
      //   { topic: "bedroom", payload: "20" },
      //   { topic: "outside", payload: "19" }
      // ]
      // //socket: io("http://localhost:5000/")
    };
  },
  mounted() {
    // this.socket.on("mqtt_message", data => {
    //   this.sensors.push(data);
    // });
  }
};
</script>
