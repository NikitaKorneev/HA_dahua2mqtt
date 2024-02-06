#!/usr/bin/with-contenv bashio

# Fetch the add-on options using the Supervisor API
CONFIG=$(curl -s -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" http://supervisor/addons/self/options)

# Export the options as environment variables
export MQTT_BROKER=$(echo $CONFIG | jq -r '.mqtt_broker')
export MQTT_PORT=$(echo $CONFIG | jq -r '.mqtt_port')
export MQTT_USERNAME=$(echo $CONFIG | jq -r '.mqtt_username')
export MQTT_PASSWORD=$(echo $CONFIG | jq -r '.mqtt_password')

export MQTT_TOPIC_FACE_RECOGNIZED=$(echo $CONFIG | jq -r '.mqtt_topic_face_recognized')
export MQTT_TOPIC_FACE_STRANGER=$(echo $CONFIG | jq -r '.mqtt_topic_face_stranger')
export MQTT_TOPIC_SMD_HUMAN=$(echo $CONFIG | jq -r '.mqtt_topic_smd_human')
export MQTT_TOPIC_SMD_CAR=$(echo $CONFIG | jq -r '.mqtt_topic_smd_car')

# Start the main Python application
python /app/app.py
