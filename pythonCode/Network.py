from Node import Node
import time
import collections

class Network:
	def __init__(self,l,slot_time,max_time,nodeCount,distanceBetweenNodes):
		self.slot_time=slot_time
		self.cur_time=0
		self.tt=80
		self.max_time=max_time
		self.collCount=0
		self.bandwidth = 100 #Mbps
		self.vel=2*(10**8)
		self.nodeCount=nodeCount
		self.distanceBetweenNodes=distanceBetweenNodes
		self.distance=collections.defaultdict(int)
		self.node=[-1]
		self.lambd=l
		for i in range(1,self.nodeCount+1):
			self.node.append(Node(i,float(self.lambd)/self.slot_time))
			self.distance[i]=(i-1)*self.distanceBetweenNodes
	
	def run(self):
		for i in range(1,self.nodeCount+1):
			self.node[i].operation(self)
		self.coll_detect()
		
		print(self.cur_time)
		for i in range(1,self.nodeCount+1):
			print("Status of Node {}: {} to {}".format(i,self.node[i].status, self.node[i].curReceiver))
			print("-------------------------------------")
		self.cur_time = self.cur_time + 1
		

	def coll_detect(self):
		collIndex=[]
		for i in range(1,self.nodeCount+1):
			if self.node[i].status=="Transmitting":
				collIndex.append(i)
		if len(collIndex)>=2:		
			self.collCount=self.collCount+1
			for i in collIndex:
				self.node[i].stopTransmit("Collision")
	
	def print_stat(self):
		for i in range(1,nodeCount+1):
			print("Total packets sent from Node {}: {}".format(i,self.node[i].packetCount-1))
			print("Average end to end throughput from Node {}: {}".format(i,self.node[i].throughput(self)))
		print("Number of collisions: ", self.collCount)
		print("Simulation end time", self.cur_time)
	
if __name__ == "__main__":
	# slot_time=int(input("Enter the slot time"))
	slot_time = 50
	l = 0.5
	distanceBetweenNodes=2000
	max_time =int(input("Enter the max time: "))
	nodeCount=int(input("Enter the number of nodes: "))
	part2=Network(l,slot_time,max_time,nodeCount,distanceBetweenNodes)	
	for _ in range(max_time+1):
	# while True:
		part2.run()
		time.sleep(1)	

	part2.print_stat()