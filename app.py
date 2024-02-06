from flask import Flask, request
import paho.mqtt.publish as publish
import json

app = Flask(__name__)

MQTT_BROKER = "192.168.100.251"
MQTT_PORT = 1883
MQTT_FACE_TOPIC = "dahua2mqtt/recognized_faces/state"
MQTT_HUMAN_TOPIC = "dahua2mqtt/smd/state"
MQTT_USERNAME = "mqtt"
MQTT_PASSWORD = "^QRLjWEsNq3Xg^hA"


@app.route('/cgi-bin/NotifyEvent', methods=['POST'])
def dahua_event():
    data = request.json
    print(f"Received data: {data}")  # For logging/debugging purposes

    # Check for FaceRecognition in the received data
    if data.get('Code') == 'FaceRecognition':
        # Create a payload for the MQTT message
        recognised_face_payload = {
            "state": "ON",  # Turn the binary sensor ON
            "attributes": {
                "person_name": data['Data']['Candidates'][0]['Person']['Name'],
                "similarity": data['Data']['Candidates'][0]['Similarity']
            }
        }

        # Publish the MQTT message
        publish.single(
            topic=MQTT_FACE_TOPIC,
            payload=json.dumps(recognised_face_payload),
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD}
        )

    elif data.get('Code') == 'SmartMotionHuman':
        smd_payload = {
            "state": "ON",  # Turn the binary sensor ON
            "attributes": {
                "nvr_channel": data['Data'][
                ['Index'],
            }
        }

        publish.single(
            topic=MQTT_HUMAN_TOPIC,
            payload=json.dumps(smd_payload),
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD}
        )

    return "Data forwarded to MQTT", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=52345)
