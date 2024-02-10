from flask import Flask, request
import paho.mqtt.publish as publish
import os
import json

# Define the path to the options.json file to get user's inputs in Configuration section
options_file_path = os.path.join(os.path.dirname(__file__), '../data/options.json')
options = {}
try:
    with open(options_file_path, 'r') as file:
        options = json.load(file)
except Exception as e:
    print(f"Error reading the options.json file: {e}")
    pass

# mqtt broker options are set up from HA addon options
MQTT_BROKER = options.get("mqtt_broker", "core-mosquitto")
MQTT_PORT = options.get("mqtt_port", 1883)
MQTT_USERNAME = options.get("mqtt_username", "mqtt")
MQTT_PASSWORD = options.get("mqtt_password", "mqtt")
AUTH = {
    'username': MQTT_USERNAME,
    'password': MQTT_PASSWORD,
}

MQTT_DISCOVERY_PREFIX = 'homeassistant'


# Function to publish MQTT discovery config
def publish_discovery_config(component, sensor_type, sensor_id, attributes):
    topic = f"{MQTT_DISCOVERY_PREFIX}/{component}/{sensor_type}_{sensor_id}/config"
    payload = {
        "name": f"{sensor_type.capitalize()} {sensor_id}",
        "state_topic": f"dahua2mqtt/{sensor_type}/{sensor_id}/state",
        "value_template": "{{ value_json.state }}",
        "json_attributes_topic": f"dahua2mqtt/{sensor_type}/{sensor_id}/state",
        "json_attributes_template": "{{ value_json.attributes | tojson }}",
        "device_class": "motion",
        "unique_id": f"dahua2mqtt_{sensor_type}_{sensor_id}"
    }
    for attribute in attributes:
        payload[attribute] = attributes[attribute]

    publish.single(topic, payload=json.dumps(payload),
                   hostname=MQTT_BROKER, port=MQTT_PORT,
                   auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD})


app = Flask(__name__)


@app.route(rule='/cgi-bin/NotifyEvent', methods=['POST'])
def dahua_event():
    data = request.json

    if data.get('Code') == 'SmartMotionHuman':
        print("SMD - Human is a GO!")
        sensor_id = data["Index"]
        sensor_type = "human_detection"
        attributes = {}

        publish_discovery_config(
            "binary_sensor",
            sensor_type,
            sensor_id,
            attributes,
        )

        topic = f"dahua2mqtt/{sensor_type}/{sensor_id}/state"
        payload = {
            "state": "ON" if data.get("Action") == "Start" else "OFF",
            "attributes": {
                "StartTime": data["Data"]["StartTime"],
                "Device id": data["Data"].get("uuid", "null"),
            }
        }

        publish.single(
            topic=topic,
            payload=json.dumps(payload),
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth=AUTH,
        )

    return "Data forwarded to MQTT", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=52345)
