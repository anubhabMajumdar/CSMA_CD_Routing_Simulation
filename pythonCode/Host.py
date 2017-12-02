from Packet import Packet
import Node

class Host(Node):
    def __init__(self, id, l):
        super(Host, self).__init__(id)
        self.lambdaVal = l  # per mu sec
        self.packet = None
        self.packetCount = 1
        self.curReceiver = None

    def startTransmit(self, wan):
        self.status = "Transmitting"
        self.curReceiver = self.selectReceiver(wan)
        self.packet = Packet(self.packetCount, (chr(ord('A')+self.curReceiver)), mac)
        self.transmissionStartTime = wan.cur_time

    def selectReceiver(self, wan):
        l = range(0, wan.nodeCount)
        l.remove(self.id)
        return random.choice(l)

    def checkPacketAvailability(self):
        return np.random.poisson(self.lambdaVal) == 1

    def operation(self, wan):
        if self.status == 'Ready' and self.checkPacketAvailability():
            self.startTransmit()
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + wan.tt + wan.curTP < wan.cur_time:
                self.status = "Ready"
                self.transmissionStartTime = 0
                self.curReceiver = None
                self.packetCount+=1
        elif self.status == 'Collision':
            self.calcBackoffTime(wan)
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime <= wan.cur_time:
            self.reStartTransmit(wan.cur_time)

    def print_status(self):
        print("Status of Router {} : {}".format(self.id,self.status))
        print("-------------------------------------")        

    def throughput(self, wan):
        total_tt = (self.packetCount-1) * wan.tt
        # tp = float((lan.distance[lan.nodeCount] - lan.distance[1])*lan.distanceBetweenNodes)/lan.vel
        tp = float((lan.nodeCount - 1) * lan.distanceBetweenNodes * (10**6))/lan.vel
        # print "TP = ", tp
        total_collisionTime = lan.collCount * 2 * tp
        total_sendTime = (self.packetCount-1) * (wan.tt + tp)
        try:
            efficiency = float(total_tt)/(total_collisionTime + total_sendTime)
            th = efficiency * lan.bandwidth
        except:
            th = -1
        return th	