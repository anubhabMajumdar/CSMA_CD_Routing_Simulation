from Node import Node
import time
import collections


class LAN:
    def __init__(self, nodeList):
        self.tt = 10
        self.collCount = 0
        self.bandwidth = 100  # Mbps
        self.vel = 2 * (10 ** 8)
        self.distance = 2000 
        self.nodeList = nodeList
        self.nodeCount = len(self.nodeList)

    def run(self, wan):
        for i in range(self.nodeCount):
            self.node[i].operation(self, wan)
        self.coll_detect()
        

    def coll_detect(self):
        collIndex = []
        for i in range(1, 5):
            if self.host[i].status == "Transmitting":
                collIndex.append(i)
            if self.router[i].status == "Transmitting":
                collIndex.append(i)    
        if len(collIndex) >= 2:
            self.collCount = self.collCount + 1
            for i in collIndex:
                self.host[i].stopTransmit("Collision")
                self.router[i].stopTransmit("Collision")

    def print_stat(self):
        for i in range(1, 5):
            print("Total packets sent from Host {}: {}".format(host[i].id, self.host[i].packetCount - 1))
            print("Average end to end throughput from Node {}: {}".format(i, self.host[i].throughput(self)))
        print("Number of collisions: ", self.collCount)