%%
node1 = Node("A", 0.5);
node2 = Node("B", 0.5);
nodes = [node1, node2];

nw = MyNetwork(2000, 200000000, 100, 50, 1000);
% tp = 10 mu sec
% tt = 80 mu sec
slotTime = 50;

%%
time = 1;
[~, nodeCount] = size(nodes);

while (time)   % time step - 1 mu sec
    %% figure out which nodes are transmitting
    for i = 1:nodeCount
        if nodes(i).status==0
            nodes(i).status = nodes(i).packetAvailability()>0;
            if nodes(i).status>0
                nodes(i).packet = Packet(1000);
                nodes(i).startTime = time;
            end
        end
        msg = nodes(i).name + " transmitting " + nodes(i).status;
        disp(msg);
    end
    
    %%
    nodes = collisionDetection(nodes);
    
    %%
    for i = 1:nodeCount
        if nodes(i).status>0 && nodes(i).startTime<time-slotTime
            nodes(i).status = 0;
            nodes(i).startTime = 0;
        end
    end
    %%
    pause(1);
    time = time + 1;
end




