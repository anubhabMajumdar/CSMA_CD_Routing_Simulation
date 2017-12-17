# Abstract

Our objective is to implement a CSMA/CD based medium access control scheme and Dijkstra routing protocol to deliver data 
between any pair of end nodes for a simulation time of 30 seconds in a virtual network. The packet movement and associated 
statistics are shown through a web simulation. The simulation has a HTML and javascript frontend which makes API call to a 
python backend to get JSON data, and uses the information to modify the GUI components accordingly. 

# Classes
* WAN
* LAN
* Node
* Host
* Router
* Packet

# Setup
* Install python 2.7+ and flask
* Start backend by typing
  ```
  python apiTest.py
  ```
* Open index.html in a browser (Tested in Chrome, Safari and Firefox)
* Click the button **Start**

# Learn more about the project
* [Demo](https://www.youtube.com/watch?v=IqFsmCidaR0)
* [Paper](https://drive.google.com/file/d/1xWWqR9Db0cJUUY8AdDigeL3foah81vFM/view?usp=sharing)
