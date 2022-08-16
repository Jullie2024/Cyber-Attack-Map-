# Cyber-Attack-Map

I completed this project as part of my summer 2022 internship. The goal of the project is to build an online map tool using MapBox API to visualize cyber attacks on an organization's honeypots. The information about the cyber attacks is stored on an Elasticsearch Server. Most of the project's code is based on Maxwell Clarke's work, which [can be viewed here](https://github.com/MatthewClarkMay/geoip-attack-map#important). Some of the code may not be optimized, mainly because l had 6 weeks to complete this project. With that being said, this project taught me how to :
* install and run linux operating system on virtual machines
* install and run Elasticsearch
* access, search, upload and retrieve files from Elasticsearch 
* search for and debug open source code
* document my work on github

#Cyber attacks visualization tool

This geoip attack map visualizer was developed to display network attacks on an organization in real time. The data server follows a syslog file, and parses out source IP, destination IP, source port, and destination port. The visualizations vary in color based on protocol type. [Click here](https://www.youtube.com/watch?v=t8NOJqvydkA) for a demo video
