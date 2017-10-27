classdef Packet
   properties
      size
      collisionCount
   end
   methods
       function obj = Packet(s)
           obj.size = s;
           obj.collisionCount = 0;
       end
   end
end