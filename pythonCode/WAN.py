import random
from Router import Router
import Host

class WAN:
    def __init__(self, host, router):
        self.cur_time = 0
        self.host = host
        self.router = router
        self.graph = {}
        self.updateGraph()
        self.createLAN(host, router)

    def createLAN(self,host, router):
        lan1list=[host[0],host[1],router[0],router[1]]
        lan2list=[host[2],host[3],router[2],router[3]]
        self.lan1=LAN(lan1list)
        self.lan2=LAN(lan2list)

    def run(self):    
        self.lan1.run(self)
        self.lan2.run(self)
        self.cur_time = self.cur_time + 1

    def updateGraph(self):
        # TP is 10 for LAN components
        self.graph = {'A': [['B', 10], ['R1', 10], ['R2', 10]],
                      'B': [['A', 10], ['R1', 10], ['R2', 10]],
                      'C': [['D', 10], ['R3', 10], ['R4', 10]],
                      'D': [['C', 10], ['R3', 10], ['R4', 10]],
                      'R1': [['A', 10], ['B', 10], ['R2', 10], ['R3', random.randint(1, 10)],
                             ['R4', random.randint(1, 10)]],
                      'R2': [['A', 10], ['B', 10], ['R1', 10], ['R3', random.randint(1, 10)],
                             ['R4', random.randint(1, 10)]],
                      'R3': [['C', 10], ['D', 10], ['R4', 10], ['R1', random.randint(1, 10)],
                             ['R2', random.randint(1, 10)]],
                      'R4': [['C', 10], ['D', 10], ['R4', 10], ['R1', random.randint(1, 10)],
                             ['R2', random.randint(1, 10)]]
                      }


# wan = WAN(None, None)
# r = Router('R2')
# for k in wan.graph.keys():
#     print k, "--->", wan.graph[k]
# r.operation(wan)

if __name__ == "__main__":
    # slot_time=int(input("Enter the slot time"))
    host=[]
    router=[]
    slot_time = 10
    lambd = 5
    for i in range(1, 5):
        host.append(Host(chr(ord('A')+i-1), float(lambd) / slot_time))
        router.append(Router("R"+str(i)))
    max_time = int(input("Enter the max time: "))
    part3=WAN(host,router)
    for _ in range(max_time + 1):
        part3.run()

    part3.print_stat()