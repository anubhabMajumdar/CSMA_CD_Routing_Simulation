classdef Node
   properties
      name
      lambda
      packet
      status
      startTime
   end
   methods
       function obj = Node(n, l)
           obj.name = n;
           obj.lambda = l;
           obj.status = 0; % Not transmitting
       end
       function [res] = packetAvailability(obj)
         res = poissrnd(obj.lambda);
      end
   end
end