class Packet:
	def __init__(self,id,size,collision_count):
		self.id=id
		self.size=size
		self.collsion_count=collision_count
	def incr_collision_count(self,collision_count):
		self.collision_count=collision_count+1
	
