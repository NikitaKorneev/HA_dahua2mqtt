# HA_dahua2mqtt

Home Assistant addon to process alarm info from Dahua's network video recorders (NVR).

Right now it works the following way
1. Addon launches Flask server that listens for a HTTP POST from the NVR.
2. Reccieved info is sent to HA's MQTT broker.
3. MQTT sensors must be configured to process the MQTT data into a sensor.

**!!!THIS IS NOT A SAFE ADDON RIGHT NOW AND A HEAVY WORK-IN_PROGRESS!!!**
