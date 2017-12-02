import numpy as np
import Packet
import random
# import WAN

class Node(object):
    def __init__(self,id):
        self.id = id
        self.status = "Ready"
        self.backoffTime = 0
        self.transmissionStartTime = 0
        self.curTP = 0

    def startTransmit(self):
        self.status = "Transmitting"

    def reStartTransmit(self, cur_time):
        print("{} is sending to {}".format(self.id,self.curReceiver))
        self.status = "Transmitting"
        self.transmissionStartTime = cur_time

    def stopTransmit(self, reason='Ready'):
        self.status = reason

    def calcBackoffTime(self, wan):
        self.packet.incr_collision_count()
        highVal = (2**self.packet.collision_count)-1
        if highVal>8:
            highVal = 8
        self.backoffTime = wan.cur_time + (np.random.randint(0, high=highVal) * wan.slot_time) # 10 is slot time
        print("Node ", self.id, "Packet id = ", self.packet.id, " Packet collision count = ", self.packet.collision_count, " backoff = ", self.backoffTime) 

    # def throughput(self, lan):
    #     total_tt = (self.packetCount-1) * lan.tt
    #     # tp = float((lan.distance[lan.nodeCount] - lan.distance[1])*lan.distanceBetweenNodes)/lan.vel
    #     tp = float((lan.nodeCount - 1) * lan.distanceBetweenNodes * (10**6))/lan.vel
    #     # print "TP = ", tp
    #     total_collisionTime = lan.collCount * 2 * tp
    #     total_sendTime = (self.packetCount-1) * (lan.tt + tp)
    #     try:
    #         efficiency = float(total_tt)/(total_collisionTime + total_sendTime)
    #         th = efficiency * lan.bandwidth
    #     except:
    #         th = -1
    #     return th


# n = Node(1, 0.5)