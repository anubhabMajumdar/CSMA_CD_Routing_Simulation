class Packet:
    def __init__(self, id, ip, mac):
        self.id = id
        self.ip = ip
        self.mac = mac
        self.hop_count = 0
        self.size = 1000
        self.collision_count = 0

    def incr_collision_count(self):
        self.collision_count += 1
