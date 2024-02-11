# Dahua2MQTT

## Overview
Dahua2MQTT is a Home Assistant add-on designed to integrate Dahua surveillance systems with Home Assistant via MQTT. It enables real-time monitoring and handling of events such as face recognition and Smart Motion Detection (SMD) directly within Home Assistant. **This add-on listens for HTTP alarms from Dahua devices (NVRs, cameras, etc.) and publishes relevant events to Home Assistant's MQTT broker**, allowing for the creation of automation triggers based on these events.
**After add-on starts, SMD and Face recognition events get published in MQTT and you can find them in Entities list under the following:**
- SmartMotionHuman
- SmartMotionCar
- FaceRecognition

## IMPORTANT:
Integrating it into Home Assistant turned out to be more difficult. As a result:
- Port selection does not work as of 0.1.0.
- User options are not imported properly. they work, but not in a good, safe way.
- Logging is not implemented and Log page on addons is not very useful right now.

## Features
- **Face Recognition**: Detects when a known or unknown face is recognized by the Dahua device.
- **Smart Motion Detection**: Identifies when motion is detected, distinguishing between human and vehicle movement.
- **Real-Time Notifications**: Sends real-time alerts to Home Assistant, enabling immediate response or automation.
- **Customizable Topics**: Allows for custom MQTT topics for different event types, providing flexibility in automation design.
- **MQTT Discovery**: Cameras with triggered SMD automatically get into Entities.

## Requirements
To use Dahua2MQTT, you'll need:
- A Dahua surveillance device (e.g., DHI-NVR5216-EI) with firmware version DH_NVR5XXX-EI_MultiLang_V4.003.0000000.0.R.231229 or compatible.
- Home Assistant with an MQTT broker set up and configured.

## Getting Started
1. **Install the Add-on**: Follow the standard procedure to install this add-on in Home Assistant.
2. **Configure MQTT**: Ensure your MQTT broker is correctly set up in Home Assistant and note the credentials.
3. **Add-on Configuration**: Input your MQTT broker details and preferred topics into the add-on's configuration.
4. **NVR setup**: Make sure Alarm Center in Settings/Network/Alarm Center/HTTP is configured and HTTP alarm is turned ON on all the cameras you need.

## Contributing
Dahua2MQTT is an open-source project, and contributions are warmly welcomed! Whether you're looking to fix bugs, add new features, or improve documentation, your help is appreciated. Please feel free to fork the repository, make your changes, and submit a pull request.

## TO-DO:
- Implement Home Assistant's MQTT Discovery feature. DONE!!!
- Implement Supervisor_token feature
- Re-work the code to be ready for when Dahua changes its HTTP API

## Support and Collaboration
If you encounter any issues or have suggestions for improvement, please file an issue on GitHub. For those looking to discuss the project, share ideas, or collaborate in any form, don't hesitate to get in touch.

## Disclaimer
This project is not affiliated with or endorsed by Dahua. It's a community-driven initiative to enhance Home Assistant integration.

## License
Dahua2MQTT is released under the Apache 2.0 License.
