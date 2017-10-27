classdef MyNetwork
   properties
      d
      v
      R
      slotTime
   end
   methods
       function obj = MyNetwork(dist, vel, dataRate, s)
           obj.d = dist;
           obj.v = vel;
           obj.R = dataRate;
           obj.slotTime = s;
       end
   end
end