from Node import Node
import time

class Network:
  def __init__(self,slot_time):
    self.tp=10 #microsec
    self.slot_time=slot_time
    self.cur_time=0
    self.tt=80
  def run(self,node1,node2):
    self.cur_time=self.cur_time+1
    self.packet_transmit(node1,node2)

  def packet_transmit(self,node1,node2):
    #decide the node to be transmitted
    #check backoff time for that node
    #if backoff time for any node is 0, then 
    #call transmit for that node
    node1.operation(self)
    node2.operation(self)
    print("Status of Node 1: ", node1.status)
    print("Status of Node 2: ", node2.status)

    # return self
    
  def coll_detect(self,node1,node2):
    if node1.status=="Transmitting" and node2.status=="Transmitting":
      node1.stop_transmit("Collision")
      node2.stop_transmit("Collision")
  def print_stat(self):
    print("Total packets sent from A: ")
    print("Total packets sent from B: ")
    print("Average end to end throughput from A to B: ")
    print("Average end to end throughput from B to A: ")
    print("Simulation end time", self.cur_time)
  
if __name__ == "__main__":
  # slot_time=int(input("Enter the slot time"))
  slot_time = 500

  part1=Network(slot_time)
  node1=Node(1,0.5/slot_time)
  node2=Node(2,0.5/slot_time)
  while(1):
    part1.run(node1,node2)
    time.sleep(1)