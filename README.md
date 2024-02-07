# Dahua2MQTT

## Overview
Dahua2MQTT is a Home Assistant add-on designed to integrate Dahua surveillance systems with Home Assistant via MQTT. It enables real-time monitoring and handling of events such as face recognition and Smart Motion Detection (SMD) directly within Home Assistant. **This add-on listens for HTTP alarms from Dahua devices (NVRs, cameras, etc.) and publishes relevant events to Home Assistant's MQTT broker**, allowing for the creation of binary sensors or automation triggers based on these events.

## Features
- **Face Recognition**: Detects when a known or unknown face is recognized by the Dahua device.
- **Smart Motion Detection**: Identifies when motion is detected, distinguishing between human and vehicle movement.
- **Real-Time Notifications**: Sends real-time alerts to Home Assistant, enabling immediate response or automation.
- **Customizable Topics**: Allows for custom MQTT topics for different event types, providing flexibility in automation design.

## Requirements
To use Dahua2MQTT, you'll need:
- A Dahua surveillance device (e.g., DHI-NVR5216-EI) with firmware version DH_NVR5XXX-EI_MultiLang_V4.003.0000000.0.R.231229 or compatible.
- Home Assistant with an MQTT broker set up and configured.
- Basic knowledge of creating and configuring binary sensors in Home Assistant.

## Getting Started
1. **Install the Add-on**: Follow the standard procedure to install this add-on in Home Assistant.
2. **Configure MQTT**: Ensure your MQTT broker is correctly set up in Home Assistant and note the credentials.
3. **Add-on Configuration**: Input your MQTT broker details and preferred topics into the add-on's configuration.
4. **Create Binary Sensors**: In Home Assistant, create binary sensors corresponding to the MQTT topics you've configured in the add-on. This will allow you to react to events from your Dahua device within Home Assistant.

## Configuration
Here's an example of the necessary configuration in `configuration.yaml` for binary sensors:

```yaml
mqtt:
  binary_sensor:
    - name: "NVR - Face recognized"
      state_topic: "dahua2mqtt/face/recognized/state"
      value_template: "{{ value_json.state }}"
      off_delay: 5  # Turns the sensor off after 5 seconds
      device_class: motion
      json_attributes_topic: "dahua2mqtt/face/recognized/state"
      json_attributes_template: "{{ value_json.attributes | tojson }}"
  
    - name: "NVR - Human detected"
      state_topic: "dahua2mqtt/smd/human/state"
      value_template: "{{ value_json.state }}"
      off_delay: 5  # Turns the sensor off after 5 seconds
      device_class: motion
```

## Contributing
Dahua2MQTT is an open-source project, and contributions are warmly welcomed! Whether you're looking to fix bugs, add new features, or improve documentation, your help is appreciated. Please feel free to fork the repository, make your changes, and submit a pull request.

## TO-DO:
- Implement Home Assistant's MQTT Discovery feature.
- Implement Supervisor_token feature
- Re-work the code to be ready for when Dahua changes its HTTP API

## Support and Collaboration
If you encounter any issues or have suggestions for improvement, please file an issue on GitHub. For those looking to discuss the project, share ideas, or collaborate in any form, don't hesitate to get in touch.

## Disclaimer
This project is not affiliated with or endorsed by Dahua. It's a community-driven initiative to enhance Home Assistant integration.

## License
Dahua2MQTT is released under the Apache 2.0 License.
