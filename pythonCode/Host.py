from Packet import Packet

class Host(Node):
    def __init__(self, id, l):
        self.lambdaVal = l  # per mu sec
        self.packet = None
        self.packetCount = 1
        self.curTP = 0
        self.curReceiver = None

    def startTransmit(self, lan):
        self.status = "Transmitting"
        self.curReceiver = self.selectReceiver(lan)
        self.curTP = ((abs(lan.distance[self.id] - lan.distance[self.curReceiver]))*lan.distanceBetweenNodes)/lan.vel
        self.packet = Packet(self.packetCount)
        self.transmissionStartTime = lan.cur_time

    def selectReceiver(self, lan):
        l = range(1, lan.nodeCount+1)
        l.remove(self.id)
        return random.choice(l)

    def checkPacketAvailability(self):
        return np.random.poisson(self.lambdaVal) == 1

    def operation(self, lan):
        if self.status == 'Ready' and self.checkPacketAvailability():
            self.startTransmit(lan)
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + lan.tt + self.curTP < lan.cur_time:
                self.status = "Ready"
                self.transmissionStartTime = 0
                self.curTP = 0
                self.curReceiver = None
                self.packetCount+=1
        elif self.status == 'Collision':
            self.calcBackoffTime(lan)
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime <= lan.cur_time:
            self.reStartTransmit(lan.cur_time)

    def print_status(self):
        print("Status of Router {} : {}".format(self.id,self.status))
        print("-------------------------------------")        

    def throughput(self, lan):
        total_tt = (self.packetCount-1) * lan.tt
        # tp = float((lan.distance[lan.nodeCount] - lan.distance[1])*lan.distanceBetweenNodes)/lan.vel
        tp = float((lan.nodeCount - 1) * lan.distanceBetweenNodes * (10**6))/lan.vel
        # print "TP = ", tp
        total_collisionTime = lan.collCount * 2 * tp
        total_sendTime = (self.packetCount-1) * (lan.tt + tp)
        try:
            efficiency = float(total_tt)/(total_collisionTime + total_sendTime)
            th = efficiency * lan.bandwidth
        except:
            th = -1
        return th	