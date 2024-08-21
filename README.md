# Dahua2MQTT - Home Assistant add-on

## Overview
Dahua2MQTT is a Home Assistant add-on designed to integrate Dahua surveillance systems with Home Assistant via MQTT. It enables real-time monitoring and handling of events such as face recognition and Smart Motion Detection (SMD) directly within Home Assistant. **This add-on listens for HTTP alarms from Dahua devices (NVRs, cameras, etc.) and publishes relevant events to Home Assistant's MQTT broker**, allowing for the creation of automation triggers based on these events.

## IMPORTANT:
This is NOT IN ANY WAY a ready solution. As of right now many thingsa are backwarkds(sic) As a result:
- Port selection does not work as of 0.1.0.
- User options are not imported properly. they work, but not in a good, safe way.
- Logging is not implemented and Log page on addons is not very useful right now.
- Add-on doesn't account for any Dahua devices other than DHI-NVR5216-EI, on which the add-on is tested.

## Requirements
To use Dahua2MQTT, you'll need:
- A Dahua surveillance device (e.g., DHI-NVR5216-EI) with firmware version DH_NVR5XXX-EI_MultiLang_V4.003.0000000.0.R.231229 or compatible. **It must support HTTP Alarm center**
- Home Assistant with an MQTT broker set up and configured.

## Getting Started
1. **Install the Add-on**: Follow the standard procedure to install this add-on in Home Assistant.
2. **Configure MQTT**: Ensure your MQTT broker is correctly set up in Home Assistant and note the credentials.
3. **Add-on Configuration**: Input your MQTT broker details, including credentials.
4. **NVR setup**: Make sure Alarm Center in Settings/Network/Alarm Center/HTTP is configured and HTTP alarm is turned ON on all the cameras you need.

## Usage
When add-on is running, whenever your NVR reports Smart Motion Detection (SMD) or Face recognition event via HTTP (**DO NOT FORGET TO SET THIS UP**),
All the channels that spot these events would appear in your HA entities list as binary sensors. Here is the schema:
- SMD:
  - Smartmotionhuman_\<channelNo.>
  - Smartmotioncar_\<channelNo>
- Face recognition:
  - Facerecognition_\<channelNo>

## Contributing
Dahua2MQTT is an open-source project, and contributions are warmly welcomed! Whether you're looking to fix bugs, add new features, or improve documentation, your help is appreciated. Please feel free to fork the repository, make your changes, and submit a pull request.

## TO-DO:
- Implement Supervisor_token feature
- Re-work the code to be ready for when Dahua changes its HTTP API
- Implement all AI detection functionalities
  - Intrusion
  - Object detection
  - ...

## Support and Collaboration
If you encounter any issues or have suggestions for improvement, please file an issue on GitHub. For those looking to discuss the project, share ideas, or collaborate in any form, don't hesitate to get in touch.

## Disclaimer
This project is not affiliated with or endorsed by Dahua. It's a community-driven initiative to enhance Home Assistant integration.
Logo and icon are made using DALI.
## License
Dahua2MQTT is released under the Apache 2.0 License.
