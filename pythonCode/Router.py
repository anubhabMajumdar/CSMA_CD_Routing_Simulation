import Packet


class Router(Node):
    def __init__(self,id):
        super(Router, self).__init__(id)
        self.route_table = {}
        self.buffer = []

    def add_packet(self, packet):
        self.buffer.append(packet)

    def update_table(self):
        return

    def routing(self, packet):
        packet.mac = self.route_table(packet.IP)

    def operation(self, wan):
        self.dijkstra(wan)
        print self.route_table

    def startTransmit(self):
        # self.status = "Transmitting"
        return

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


