classdef MyNetwork
   properties
      d % in meters
      v % in m/sec
      R % in Mbps
      slotTime % in mu sec
      tp
      tt
   end
   methods
       function obj = MyNetwork(dist, vel, dataRate, s, packetSize)
           obj.d = dist;
           obj.v = vel;
           obj.R = dataRate;
           obj.slotTime = s;
           obj.tp = dist/vel;
           obj.tt = packetSize/dataRate;
       end
   end
end