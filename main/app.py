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

# Main section that sets up topics for appropriate "AI" events from NVR according to add-on configuration
MQTT_TOPIC_FACE_RECOGNIZED = options.get("mqtt_topic_face_recognized", "dahua2mqtt/face/recognized/state")
MQTT_TOPIC_FACE_STRANGER = options.get("mqtt_topic_face_stranger", "dahua2mqtt/face/stranger/state")
MQTT_TOPIC_SMD_HUMAN = options.get("mqtt_topic_smd_human", "dahua2mqtt/smd/human/state")
MQTT_TOPIC_SMD_CAR = options.get("mqtt_topic_smd_car", "dahua2mqtt/smd/car/state")
all_topics = [
    MQTT_TOPIC_FACE_RECOGNIZED,
    MQTT_TOPIC_FACE_STRANGER,
    MQTT_TOPIC_SMD_HUMAN,
    MQTT_TOPIC_SMD_CAR,
]


def topic_reset():
    for topic in all_topics:  # Sets MQTT state for all the topics as OFF
        reset_payload = {
            "state": "OFF",
        }

        publish.single(
            topic=topic,
            payload=json.dumps(reset_payload),
            hostname=MQTT_BROKER,
            port=MQTT_PORT,
            auth={
                'username': MQTT_USERNAME,
                'password': MQTT_PASSWORD,
            }
        )


app = Flask(__name__)

print("Addon started. Listening...")
topic_reset()


@app.route(
    rule='/cgi-bin/NotifyEvent',
    methods=['POST']
)
def dahua_event():
    data = request.json
    # print(f"Received data: Action: {data.get('Action')}, {data.get('Code')}")  # For logging/debugging purposes
    # FACE RECOGNITION SECTION
    if data.get('Code') == 'FaceRecognition':

        if data["Data"]["Candidates"]:  # Event if face is recognized

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

        else:  # Event if face is NOT recognized
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
    topic_reset()
    return "Data forwarded to MQTT", 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=52345)
