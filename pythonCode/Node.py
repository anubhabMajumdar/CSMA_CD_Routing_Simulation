import numpy as np
import Packet
import Network

class Node:
    def __init__(self, id, l):
        self.id = id
        self.lambdaVal = l  # per mu sec
        self.packet = None
        self.status = "Ready"
        self.backoffTime = 0
        self.transmissionStartTime = 0
        self.packetCount = 1

    def startTransmit(self, curTime):
        self.status = "Transmitting"
        self.packet = Packet(self.packetCount)
        self.transmissionStartTime = curTime

    def reStartTransmit(self, curTime):
        self.status = "Transmitting"
        self.transmissionStartTime = curTime

    def stopTransmit(self, reason='Ready'):
        self.status = reason
        self.packet = None

    def checkPacketAvailability(self):
        return np.random.poisson(self.lambdaVal) == 1

    def calcBackoffTime(self, nw):
        self.backoffTime = nw.cur_time + (np.random.randint(0, high=(2**self.packet.collision_count)-1) * nw.slot_time)

    def operation(self, nw):
        if self.status == 'Ready' and self.checkPacketAvailability():
            self.startTransmit(nw.curTime)
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + nw.tt + nw.tp < nw.curTime:
                self.status = "Ready"
                self.transmissionStartTime = 0
        elif self.status == 'Collision':
            self.calcBackoffTime()
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime == nw.curTime:
            self.reStartTransmit(nw.curTime)






n = Node(1, 0.5)


