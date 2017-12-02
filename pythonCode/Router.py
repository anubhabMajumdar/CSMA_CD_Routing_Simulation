import Packet
from WAN import WAN

class Router(Node):
    def __init__(self,id):
        super(Router, self).__init__(id)
        self.route_table = {}
        self.curPacket = None
        self.transmissionStartTime = 0
        self.packetCount = 1
        self.status
        self.buffer = []
        
    def update_table(self):
        return

    def add_packet(self, packet):
        self.buffer.append(packet)

    def routing(self, packet):
        packet.mac = self.route_table(packet.IP)

    def operation(self, wan):
        if self.status == 'Ready' and len(self.buffer)>0:
            self.startTransmit(wan)
        elif self.status == 'Transmitting':
            if self.transmissionStartTime + wan.tt + self.curTP < wan.cur_time:
                self.status = "Ready"
                self.transmissionStartTime = 0
                send_to = self.curPacket.mac
                if send_to.startswith('R'):
                    idx = int(send_to[-1])-1
                    wan.router[idx].add_packet(self.curPacket)
        elif self.status == 'Collision':
            self.calcBackoffTime(wan)
            self.status = 'Waiting'
        elif self.status == 'Waiting' and self.backoffTime <= wan.cur_time:
            self.reStartTransmit(wan.cur_time)

    def startTransmit(self, wan):
        self.dijkstra(wan)

        self.curPacket = self.buffer[0]
        del self.buffer[0]

        self.routing(self.curPacket)

        self.status = 'Transmitting'
        self.transmissionStartTime = wan.cur_time



    def dijkstra(self, wan):
        class DijkstraNode:
            def __init__(self, id, cost, path):
                self.id = id
                self.cost = cost
                self.path = path

            def __cmp__(self, other):
                return cmp(self.cost, other.cost)

        end_nodes = ['A', 'B', 'C', 'D']
        nodes = [DijkstraNode(self.id, 0, [self.id])]
        visited = []
        while len(nodes) > 0:
            cur = min(nodes, key=lambda x: x.cost)
            # idx = nodes.index(cur)
            nodes.remove(cur)

            visited.append(cur.id)
            if cur.id in end_nodes:
                self.route_table[cur.id] = cur.path[1]
            else:
                for n, c in wan.graph[cur.id]:
                    if n in visited:
                        continue
                    else:
                        p = cur.path[:]
                        p.append(n)
                        flag = True
                        for i in nodes:
                            if i.id == n:
                                flag = False
                                if i.cost > cur.cost + c:
                                    i.cost = cur.cost + c
                        if flag:
                            temp = DijkstraNode(n, cur.cost + c, p)
                            nodes.append(temp)


