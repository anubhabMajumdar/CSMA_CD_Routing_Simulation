function [nodes] = collisionDetection(nodes)
    
    [~, nodeCount] = size(nodes);
    
    count = 0;
    for i = 1:nodeCount
       if nodes(i).status > 0
        count = count + 1;
       end
    end
    
    if count<=1
       disp("No collision");
       return;
    end
    
    for i = 1:nodeCount
       if nodes(i).status > 0
        nodes(i).packet.collisionCount = nodes(i).packet.collisionCount + 1;
        nodes(i).status = 0;
        nodes(i).startTime = 0;
       end
    end
    disp("Collision");
    return;
end