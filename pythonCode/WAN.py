import random


class WAN:
    def __init__(self, lan1, lan2):
        self.lan1 = lan1
        self.lan2 = lan2
        self.graph = {}
        self.updateGraph()

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
