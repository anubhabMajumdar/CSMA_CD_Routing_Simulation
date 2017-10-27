classdef Packet
   properties
      size
   end
   methods
       function obj = Packet(s)
           obj.size = s;
       end
   end
end