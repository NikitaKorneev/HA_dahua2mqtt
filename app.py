from flask import Flask, request
import paho.mqtt.publish as publish
import os

app = Flask(__name__)

MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "dahua2mqtt/"
MQTT_USERNAME = os.getenv('OPTIONS_MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('OPTIONS_MQTT_PASSWORD')


@app.route('/cgi-bin/NotifyEvent', methods=['POST'])
def dahua_event():
    data = request.json
    print(f"Received data: {data}")  # For logging/debugging purposes
    publish.single(MQTT_TOPIC, payload=str(data), hostname=MQTT_BROKER, port=MQTT_PORT, auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD})
    return "Data forwarded to MQTT", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=52345)
