import Packet
class Router:
	def __init__(self,id):
		self.id=id
		self.route_table=[]
		self.buffer=[]
		
	def add_packet(self,packet):
		self.buffer.append(packet)

	def update_table(self):

	def routing(self,packet):
		packet.IP=self.route_table(packet.IP) 

	def operation(self):

	def startTransmit(self,):
        self.status = "Transmitting"			
