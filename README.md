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

## To Deploy the Tool

I ran my code on Linux 20.04 LTS and using python 3.8

Clone the application
*       git clone https://github.com/matthewclarkmay/geoip-attack-map.git
Install system dependencies
*       sudo apt install python3-pip redis-server
Install python requirements:
*       cd geoip-attack-map
        sudo pip3 install -U -r requirements.txt
Start Redis Server:
*       redis-server
Configure the Data Server DB:
*       cd DataServerDB
        ./db-dl.sh
        cd ..   
Start the Data Server:
*       cd DataServer
        sudo python3 DataServer.py
Start the Syslog Gen Script, inside DataServer directory:
  Open a new terminal tab (Ctrl+Shift+T, on Ubuntu).
*       ./syslog-gen.py   
Configure the Attack Map Server, extract the flags to the right place:
  Open a new terminal tab (Ctrl+Shift+T, on Ubuntu).
*       cd AttackMapServer/
        unzip static/flags.zip : make sure the unzipped file is still inside AttackMapServer
Start the Attack Map Server:
*       sudo python3 AttackMapServer.py



Access the Attack Map Server from browser:

http://localhost:8888/ or http://127.0.0.1:8888/

To access via browser on another computer, use the external IP of the machine running the AttackMapServer.

Edit the IP Address in the file "/static/map.js" at "AttackMapServer" directory. From:

var webSock = new WebSocket("ws:/127.0.0.1:8888/websocket");
To, for example:

var webSock = new WebSocket("ws:/192.168.1.100:8888/websocket");
Restart the Attack Map Server:

sudo python3 AttackMapServer.py
On the other computer, points the browser to:

http://192.168.1.100:8888/
