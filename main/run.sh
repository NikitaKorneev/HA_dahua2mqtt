#!/bin/bash

# Fetch the add-on options using the Supervisor API
CONFIG=$(curl -s -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" http://supervisor/addons/self/options)

# Export the options as environment variables
export MQTT_BROKER=$(echo $CONFIG | jq -r '.mqtt_broker')
export MQTT_PORT=$(echo $CONFIG | jq -r '.mqtt_port')
export MQTT_USERNAME=$(echo $CONFIG | jq -r '.mqtt_username')
export MQTT_PASSWORD=$(echo $CONFIG | jq -r '.mqtt_password')
# ... add other configuration options as needed

# Start the main Python application
python3 app.py