from Node import Node
import time
import collections


class LAN:
    def __init__(self, l, slot_time, max_time):
        self.slot_time = slot_time
        self.cur_time = 0
        self.tt = 10
        self.max_time = max_time
        self.collCount = 0
        self.bandwidth = 100  # Mbps
        self.vel = 2 * (10 ** 8)
        self.distance = 2000
        self.node=[]
        self.lambd = l
        for i in range(1, 5):
            self.node.append(Host(chr(ord('A')+i-1), float(self.lambd) / self.slot_time))
            self.node.append(Router("R"+str(i)))
        self.nodeCount=len(self.node)   

    def run(self):
        for i in range(1, self.nodeCount+1):
            self.node[i].operation(self)
        self.coll_detect()

        print(self.cur_time)
        self.cur_time = self.cur_time + 1

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
            print("Total packets sent from Node {}: {}".format(i, self.host[i].packetCount - 1))
            print("Average end to end throughput from Node {}: {}".format(i, self.node[i].throughput(self)))
        print("Number of collisions: ", self.collCount)
        print("Simulation end time", self.cur_time)


if __name__ == "__main__":
    # slot_time=int(input("Enter the slot time"))
    slot_time = 10
    l = 5
    max_time = int(input("Enter the max time: "))
    delayFlag = raw_input("Delay (y/n): ")
    part3 = LAN(l, slot_time, max_time)
    for _ in range(max_time + 1):
        # while True:
        part3.run()
        if delayFlag == 'y' or delayFlag == 'Y':
            time.sleep(1)

    part2.print_stat()
