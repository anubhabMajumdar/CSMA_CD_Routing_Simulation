import Packet
from Node import Node as Node
import WAN
import Router
import numpy as np
import random

class Host(Node):
    def __init__(self, id, l):
        super(Host, self).__init__(id)
        self.lambdaVal = l  # per mu sec
        self.packet = None
        self.packetCount = 0
        self.curReceiver = None
        self.mac = id
        self.ip = id
        self.next_hop_mac=None
        self.curThroughput = 0
        self.totalCollision = 0

    def startTransmit(self, wan):
        self.status = "Transmitting"
        self.curReceiver = self.selectReceiver(wan).id
        print("{} is sending to {}".format(self.id,self.curReceiver))
        if self.id == "A":
            self.next_hop_mac = "R1"
        elif self.id == "B":
            self.next_hop_mac = "R2"
        elif self.id == "C":
            self.next_hop_mac = "R3"
        elif self.id == "D":
            self.next_hop_mac = "R4"          
        self.packet = Packet.Packet(self.packetCount, self.curReceiver, self.next_hop_mac)
        self.transmissionStartTime = wan.cur_time

    def selectReceiver(self, wan):
        temp = wan.host[:]
        temp.remove(self)
        return random.choice(temp)

    def checkPacketAvailability(self):
        return np.random.poisson(self.lambdaVal) == 1

    def operation(self, wan):
        print("{}: Status of Node {} is {} ".format(wan.cur_time,self.id,self.status))
        if self.status == 'Ready' and self.checkPacketAvailability():
            self.startTransmit(wan)
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + wan.tt + wan.tp < wan.cur_time:
                wan.router[int(self.next_hop_mac[1])-1].add_packet(self.packet)
                wan.router[int(self.next_hop_mac[1])-1].receivedPacketCount+=1
                self.status = "Ready"
                self.transmissionStartTime = 0
                self.curReceiver = None
                self.packetCount+=1
                self.packet=None
        elif self.status == 'Collision':
            self.totalCollision+=1
            self.calcBackoffTime(wan)
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime <= wan.cur_time:
            self.reStartTransmit(wan.cur_time)

        self.curThroughput = self.throughput(wan)  

    def print_status(self):
        print("Status of Router {} : {}".format(self.id,self.status))
        print("-------------------------------------")        

    def throughput(self, wan):
        total_tt = (self.packetCount) * wan.tt
        # tp = float((lan.distance[lan.nodeCount] - lan.distance[1])*lan.distanceBetweenNodes)/lan.vel
        tp = wan.tp
        # print "TP = ", tp
        total_collisionTime = self.totalCollision * 2 * tp
        total_sendTime = (self.packetCount) * (wan.tt + tp)
        try:
            efficiency = float(total_tt)/(total_collisionTime + total_sendTime)
            th = efficiency * wan.lan1.bandwidth
        except:
            th = 0.0
        # print self.id, " -----> ", th
        return round(th, 2)