from flask import Flask, request
import paho.mqtt.publish as publish
import os
import json
print(os.getcwd())
print(os.listdir())
app = Flask(__name__)
# mqtt broker options are set up from HA addon options
MQTT_BROKER = os.getenv("OPTIONS_MQTT_BROKER")
MQTT_PORT = os.getenv("OPTIONS_MQTT_PORT")
MQTT_USERNAME = os.getenv("OPTIONS_MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("OPTIONS_MQTT_PASSWORD")
print(f"Imported conf vars:\n{MQTT_BROKER}\n{MQTT_PORT}\n{MQTT_USERNAME}\n{MQTT_PASSWORD}")

# Main section that sets up topics for appropriate "AI" events from NVR
MQTT_TOPIC_FACE_RECOGNIZED = os.getenv("OPTIONS_MQTT_TOPIC_FACE_RECOGNIZED")
MQTT_TOPIC_FACE_STRANGER = os.getenv("OPTIONS_MQTT_TOPIC_FACE_STRANGER")
MQTT_TOPIC_SMD_HUMAN = os.getenv("OPTIONS_MQTT_TOPIC_SMD_HUMAN")
MQTT_TOPIC_SMD_CAR = os.getenv("OPTIONS_MQTT_TOPIC_SMD_CAR")


@app.route(
    rule='/cgi-bin/NotifyEvent',
    methods=['POST']
)
def dahua_event():
    data = request.json
    print(f"Received data: Action: {data.get('Action')}, {data.get('Code')}")  # For logging/debugging purposes

    # Check for FaceRecognition in the received data
    if data.get('Code') == 'FaceRecognition':
        # Event if face is recognized
        if data["Data"]["Candidates"]:
            # Create a payload for the MQTT message
            recognised_face_payload = {
                "state": "ON",  # Turn the binary sensor ON
                "attributes": {  # Report name and similarity % as attributes
                    "person_name": data['Data']['Candidates'][0]['Person']['Name'],
                    "similarity": data['Data']['Candidates'][0]['Similarity']
                }
            }

            # Publish the MQTT message
            publish.single(
                topic=MQTT_TOPIC_FACE_RECOGNIZED,
                payload=json.dumps(recognised_face_payload),
                hostname=MQTT_BROKER,
                port=MQTT_PORT,
                auth={
                    'username': MQTT_USERNAME,
                    'password': MQTT_PASSWORD,
                }
            )

        else:
            stranger_face_payload = {
                "state": "ON",  # Turn the binary sensor ON
            }
            # Publish the MQTT message
            publish.single(
                topic=MQTT_TOPIC_FACE_STRANGER,
                payload=json.dumps(stranger_face_payload),
                hostname=MQTT_BROKER,
                port=MQTT_PORT,
                auth={
                    'username': MQTT_USERNAME,
                    'password': MQTT_PASSWORD,
                }
            )

    elif data.get('Code') == 'SmartMotionHuman':
        smd_human_payload = {
            "state": "ON",  # Turn the binary sensor ON
        }

        publish.single(
            topic=MQTT_TOPIC_SMD_HUMAN,
            payload=json.dumps(smd_human_payload),
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={
                'username': MQTT_USERNAME,
                'password': MQTT_PASSWORD,
            }
        )

    elif data.get('Code') == 'SmartMotionCar':
        smd_car_payload = {
            "state": "ON",  # Turn the binary sensor ON
        }

        publish.single(
            topic=MQTT_TOPIC_SMD_HUMAN,
            payload=json.dumps(smd_car_payload),
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={
                'username': MQTT_USERNAME,
                'password': MQTT_PASSWORD
            }
        )

    return "Data forwarded to MQTT", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=52345)
