import numpy as np
from Packet import Packet
import random
# import Network

class Node:
    def __init__(self, id, l):
        self.id = id
        self.lambdaVal = l  # per mu sec
        self.packet = None
        self.status = "Ready"
        self.backoffTime = 0
        self.transmissionStartTime = 0
        self.packetCount = 1
        self.curTP = 0
        self.curReceiver = None

    def startTransmit(self, nw):
        self.status = "Transmitting"
        self.curReceiver = self.selectReceiver(nw)
        self.curTP = ((abs(nw.distance[self.id] - nw.distance[self.curReceiver]))*nw.distanceBetweenNodes)/nw.vel
        self.packet = Packet(self.packetCount)
        self.transmissionStartTime = nw.cur_time

    def selectReceiver(self, nw):
        l = range(1, nw.nodeCount+1)
        l.remove(self.id)
        return random.choice(l)

    def reStartTransmit(self, cur_time):
        self.status = "Transmitting"
        self.transmissionStartTime = cur_time

    def stopTransmit(self, reason='Ready'):
        self.status = reason

    def checkPacketAvailability(self):
        return np.random.poisson(self.lambdaVal) == 1

    def calcBackoffTime(self, nw):
        self.packet.incr_collision_count()
        highVal = (2**self.packet.collision_count)-1
        if highVal>8:
            highVal = 8
        self.backoffTime = nw.cur_time + (np.random.randint(0, high=highVal) * nw.slot_time)
        print("Node ", self.id, "Packet id = ", self.packet.id, " Packet collision count = ", self.packet.collision_count, " backoff = ", self.backoffTime)

    def operation(self, nw):
        if self.status == 'Ready' and self.checkPacketAvailability():
            self.startTransmit(nw)
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + nw.tt + self.curTP < nw.cur_time:
                self.status = "Ready"
                self.transmissionStartTime = 0
                self.curTP = 0
                self.curReceiver = None
                self.packetCount+=1
        elif self.status == 'Collision':
            self.calcBackoffTime(nw)
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime <= nw.cur_time:
            self.reStartTransmit(nw.cur_time)

    def throughput(self, nw):
        total_tt = (self.packetCount-1) * nw.tt
        tp = float((nw.distance[nw.nodeCount] - nw.distance[1])*nw.distanceBetweenNodes)/nw.vel
        total_collisionTime = nw.collCount * 2 * tp
        total_sendTime = (self.packetCount-1) * (nw.tt + tp)
        try:
            efficiency = float(total_tt)/(total_collisionTime + total_sendTime)
            th = efficiency * nw.bandwidth
        except:
            th = -1
        return th




# n = Node(1, 0.5)


