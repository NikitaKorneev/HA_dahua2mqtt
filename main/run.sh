#!/usr/bin/with-contenv bashio

# Fetch the add-on options using the Supervisor API
CONFIG_PATH=/data/options.json

# Export the options as environment variables
MQTT_BROKER="$(bashio::config 'mqtt_broker')"
MQTT_PORT="$(bashio::config 'mqtt_port')"
MQTT_USERNAME="$(bashio::config 'mqtt_username')"
MQTT_PASSWORD="$(bashio::config 'mqtt_password')"

MQTT_TOPIC_FACE_RECOGNIZED="$(bashio::config 'mqtt_topic_face_recognized')"
MQTT_TOPIC_FACE_STRANGER="$(bashio::config 'mqtt_topic_face_stranger')"
MQTT_TOPIC_SMD_HUMAN="$(bashio::config 'mqtt_topic_smd_human')"
MQTT_TOPIC_SMD_CAR="$(bashio::config 'mqtt_topic_smd_car')"

# Start the main Python application
python /app/app.py
