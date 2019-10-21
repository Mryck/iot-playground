import eventlet
import json
from flask_mqtt import Mqtt
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

eventlet.monkey_patch()

app = Flask(__name__)

app.config["MQTT_BROKER_URL"] = "mosquitto"
app.config["MQTT_BROKER_PORT"] = 1883
app.config["MQTT_CLIENT_ID"] = "flask_mqtt"
app.config["MQTT_KEEPALIVE"] = 5
app.config["MQTT_TLS_ENABLED"] = False

app.config["SECRET_KEY"] = "secret!"
mqtt = Mqtt(app)
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True)


@socketio.on("message")
def handle_message(message):
    emit("testResponse", "OK")


@socketio.on("subscribe")
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data["topic"], data["qos"])


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(topic=message.topic, payload=message.payload.decode(), qos=message.qos)
    socketio.emit("mqtt_message", data=data)


@socketio.on("unsubscribe_all")
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
