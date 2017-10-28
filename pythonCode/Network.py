class Network:
  import Node
  def __init__(self):
    self.tp=10 #microsec
    self.rate=100 #so when you divide, you directly get the value in microsec
    self.cur_time=0
    self.tt=80
  def run(self):
    self.cur_time=self.cur_time+1
  def packet_transmit(self,node1,node2):
    #decide the node to be transmitted
    #check backoff time for that node
    #if backoff time for any node is 0, then 
    #call transmit for that node
    node1.operation()
    node2.operation()
    return self
    
  def coll_detect(self,node1,node2):
    if node1.status=="transmitting" and node2.status=="transmitting":
      node1.stop_transmit("collision")
      node2.stop_transmit("collision")
  def print_stat(self):
    print("Total packets sent from A")
    print("Total packets sent from B")
    print("Average end to end throughput from A to B")
    print("Average end to end throughput from A to B")
    print("Simulation end time", self.cur_time)
  
if __name__ == "__main__":
  part1=Network()
  while(1):
    part1.run()