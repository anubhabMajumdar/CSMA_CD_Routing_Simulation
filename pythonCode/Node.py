import numpy as np
from Packet import Packet
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

    def startTransmit(self, cur_time):
        self.status = "Transmitting"
        self.packet = Packet(self.packetCount)
        self.packetCount+=1
        self.transmissionStartTime = cur_time

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
            self.startTransmit(nw.cur_time)
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + nw.tt + nw.tp < nw.cur_time:
                self.status = "Ready"
                self.transmissionStartTime = 0
        elif self.status == 'Collision':
            self.calcBackoffTime(nw)
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime <= nw.cur_time:
            self.reStartTransmit(nw.cur_time)






# n = Node(1, 0.5)


