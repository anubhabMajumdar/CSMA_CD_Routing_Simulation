class Packet:
	def __init__(self,id,size=1000):
		self.id=id
		self.size=size
		self.collsion_count = 0

	def incr_collision_count(self,collision_count):
		self.collision_count=collision_count+1
	
