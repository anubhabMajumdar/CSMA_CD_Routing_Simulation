classdef Node
   properties
      name
      lambda
   end
   methods
       function obj = Node(n, l)
           obj.name = n;
           obj.lambda = l;
       end
       function [res] = packetAvailability(obj)
         res = poissrnd(obj.lambda);
      end
   end
end