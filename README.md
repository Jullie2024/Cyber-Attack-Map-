# Cyber-Attack-Map

I completed this project as part of my summer 2022 internship. The goal of the project is to build an online map tool using MapBox API to visualize cyber attacks on an organization's honeypots. The information about the cyber attacks is stored on an Elasticsearch Server. Most of the project's code is based on Maxwell Clarke's work, which [can be viewed here](https://github.com/MatthewClarkMay/geoip-attack-map#important). Some of the code may not be optimized, mainly because l had 6 weeks to complete this project. With that being said, this project taught me how to :
* install and run linux operating system on virtual machines
* install and run Elasticsearch
* access, search, upload and retrieve files from Elasticsearch 
* search for and debug open source code
* document my work on github

## Cyber attacks visualization tool

This geoip attack map visualizer was developed to display network attacks on an organization in real time. The data server follows a syslog file, and parses out source IP, destination IP, source port, and destination port. The visualizations vary in color based on protocol type. [Click here](https://www.youtube.com/watch?v=t8NOJqvydkA) for a demo video

## Important information
This program relies entirely on syslog, and because all appliances format logs differently, you will need to customize the log parsing function(s). If your organization uses a security information and event management system (SIEM), it can probably normalize logs to save you a ton of time writing regex.

* Send all syslog to SIEM.
* Use SIEM to normalize logs.
* Send normalized logs to the box (any Linux machine running syslog-ng will work) running this software so the data server can parse them.

## Configuration
* You can run the DataServer on a different machine than the AttackMapServer. Change the bind in /etc/redis/redis.conf from change bind 127.0.0.1 to bind 0.0.0.0
* Make sure that the WebSocket address in /AttackMapServer/index.html points back to the IP address of the AttackMapServer.
* Add headquarters latitude/longitude to hqLatLng variable in index.html
* Use syslog-gen.py to push your own data to syslog or visualize your own data on the map


