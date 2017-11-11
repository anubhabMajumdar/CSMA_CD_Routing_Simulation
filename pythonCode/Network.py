from Node import Node
import time

class Network:
	def __init__(self,slot_time,max_time):
		self.tp=10 #microsec
		self.slot_time=slot_time
		self.cur_time=0
		self.tt=80
		self.max_time=max_time
		self.collCount=0
		self.bandwidth = 100 #Mbps
	
	def run(self,node1,node2):
		self.packet_transmit(node1,node2)
		self.cur_time = self.cur_time + 1

	def packet_transmit(self,node1,node2):
		#decide the node to be transmitted
		#check backoff time for that node
		#if backoff time for any node is 0, then 
		#call transmit for that node
		node1.operation(self)
		node2.operation(self)
		self.coll_detect(node1, node2)

		print(self.cur_time)
		print("Status of Node 1: ", node1.status)
		print("Status of Node 2: ", node2.status)
		print("-------------------------------------")
		print("-------------------------------------")
		# return self
		
	def coll_detect(self,node1,node2):
		if node1.status=="Transmitting" and node2.status=="Transmitting":
			self.collCount=self.collCount+1
			node1.stopTransmit("Collision")
			node2.stopTransmit("Collision")
	
	def print_stat(self, node1, node2):
		print("Total packets sent from A: ", node1.packetCount-1)
		print("Total packets sent from B: ", node2.packetCount-1)
		print("Number of collisions: ", self.collCount)
		print("Average end to end throughput from A to B: ", node1.throughput(self))
		print("Average end to end throughput from B to A: ", node2.throughput(self))
		print("Simulation end time", self.cur_time)
	
if __name__ == "__main__":
	# slot_time=int(input("Enter the slot time"))
	slot_time = 50
	l = 0.5
	max_time =int(input("Enter the max time: "))
	part1=Network(slot_time,max_time)
	node1=Node(1,l/slot_time)
	node2=Node(2,l/slot_time)
	for _ in range(max_time+1):
		part1.run(node1,node2)
		# time.sleep(1)	

	part1.print_stat(node1, node2)