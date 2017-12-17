from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.json import jsonify
from flask import render_template
from flask_cors import CORS
import WAN

app = Flask(__name__)
CORS(app)
api = Api(app)

count = 0

@app.route("/", methods=['GET'])
def networkStatus():
	# print request.remote_addr
	wan = WAN.runCodeRun()
	if wan.cur_time==3000001:
		return
	d = {}
	for i in range(4):
		if wan.lan1.nodeList[i].packet != None:
			d[wan.lan1.nodeList[i].id] = {
				"status": wan.lan1.nodeList[i].status, 
				"to": wan.lan1.nodeList[i].curReceiver,
				"id": wan.lan1.nodeList[i].packet.id,
				"IP": wan.lan1.nodeList[i].packet.ip,
				"MAC": wan.lan1.nodeList[i].packet.mac,
				"collisionCount": wan.lan1.nodeList[i].packet.collision_count,
				"packetCount": wan.lan1.nodeList[i].packetCount,
				"receivedPacketCount": wan.lan1.nodeList[i].receivedPacketCount
				}
		else:
			d[wan.lan1.nodeList[i].id] = {
				"status": wan.lan1.nodeList[i].status, 
				"to": wan.lan1.nodeList[i].curReceiver,
				"id": "",
				"IP": "",
				"MAC": "",
				"collisionCount": "",
				"packetCount": wan.lan1.nodeList[i].packetCount,
				"receivedPacketCount": wan.lan1.nodeList[i].receivedPacketCount
				}
		if wan.lan2.nodeList[i].packet != None:
			d[wan.lan2.nodeList[i].id] = {
				"status": wan.lan2.nodeList[i].status, 
				"to": wan.lan2.nodeList[i].curReceiver,
				"id": wan.lan2.nodeList[i].packet.id,
				"IP": wan.lan2.nodeList[i].packet.ip,
				"MAC": wan.lan2.nodeList[i].packet.mac,
				"collisionCount": wan.lan2.nodeList[i].packet.collision_count,
				"packetCount": wan.lan2.nodeList[i].packetCount,
				"receivedPacketCount": wan.lan2.nodeList[i].receivedPacketCount
				}
		else:
			d[wan.lan2.nodeList[i].id] = {
				"status": wan.lan2.nodeList[i].status, 
				"to": wan.lan2.nodeList[i].curReceiver,
				"id": "",
				"IP": "",
				"MAC": "",
				"collisionCount": "",
				"packetCount": wan.lan2.nodeList[i].packetCount,
				"receivedPacketCount": wan.lan2.nodeList[i].receivedPacketCount
				}
	d['time'] = wan.cur_time

	g = {}
	n =  ['A', 'B', 'C', 'D', 'R1', 'R2', 'R3', 'R4']
	for i in n:
		g[i] = {}
		for j in n:
			if i==j:
				g[i][j] = 0
			else:
				g[i][j] = 'inf'

	for i in n:
		vals = wan.graph[i]
		for j in vals:
			neighbour = j[0]
			cost = j[1]
			g[i][neighbour] = cost

	d['graph'] = g

	for i in wan.router:
		d[i.id+"_route_table"] = i.route_table
	
	for i in wan.host:
		d[i.id+"_throughput"] = i.curThroughput
	return jsonify(d)


if __name__ == '__main__':
	 app.run(port=5002)