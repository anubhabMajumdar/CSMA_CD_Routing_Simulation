import Node
import time
import collections
import WAN


class LAN:
    def __init__(self, nodeList):
        self.collCount = 0
        self.bandwidth = 100  # Mbps
        self.nodeList = nodeList
        self.nodeCount = len(self.nodeList)

    def run(self, wan):
        for i in range(self.nodeCount):
            self.nodeList[i].operation(wan)
        print("-----------------------------------------------------")    
        self.coll_detect()
        

    def coll_detect(self):
        collIndex = []
        for i in range(4):
            if self.nodeList[i].status == "Transmitting":
                collIndex.append(i)   
        if len(collIndex) >= 2:
            self.collCount = self.collCount + 1
            for i in collIndex:
                if self.nodeList[i].id.startswith("R"):
                    if not self.nodeList[i].curReceiver.startswith("R"):
                        self.nodeList[i].stopTransmit("Collision")
                else:
                    self.nodeList[i].stopTransmit("Collision")

    def print_stat(self):
        for i in range(1, 5):
            print("Total packets sent from Node {}: {}".format(self.nodeList[i].id, self.nodeList[i].packetCount - 1))
            #print("Average end to end throughput from Node {}: {}".format(i, self.host[i].throughput(self)))
        print("Number of collisions: ", self.collCount)