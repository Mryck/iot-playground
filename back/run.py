# coding: utf-8

"""Backend code to intercat with mqtt and serve info to the front end."""

import eventlet
import json
from flask_mqtt import Mqtt
from flask import Flask
from flask_socketio import SocketIO

eventlet.monkey_patch()

app = Flask(__name__)

# Basic configuration for flask_mqtt
app.config['MQTT_BROKER_URL'] = 'mosquitto'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_CLIENT_ID'] = 'flask_mqtt'
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)

# Setup socket io to allow cors origni from anywhere and print log
socketio = SocketIO(app, cors_allowed_origins='*', engineio_logger=True)


@socketio.on('subscribe')
def handle_subscribe(json_str):
    """Mqtt subscribe to the given topic send from socketio."""
    mqtt_data = json.loads(json_str)
    mqtt.subscribe(mqtt_data['topic'], mqtt_data['qos'])


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    """Mqtt unsubscribe to all topic."""
    mqtt.unsubscribe_all()


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    """Send socketio request on mqtt message."""
    json_data = {
        'topic': message.topic,
        'payload': message.payload.decode(),
        'qos': message.qos,
    }
    socketio.emit('mqtt_message', data=json_data)


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    """Log mqtt message."""
    print(level, buf)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
