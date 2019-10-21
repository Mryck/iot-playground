import Vue from 'vue'
import App from './App.vue'
import './../node_modules/bulma/css/bulma.css'
import socketio from 'socket.io-client';
import VueSocketIO from 'vue-socket.io';

export const SocketInstance = socketio('http://localhost:5000');

Vue.use(new VueSocketIO({
  debug: true,
  connection: SocketInstance
})
);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
