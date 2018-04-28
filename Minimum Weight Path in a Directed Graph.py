from collections import defaultdict
from heapq import *

def shortest_path(edges,start_from,end_to):
    
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,start_from,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == end_to:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")


first_line=input("g_nodes g_edge :")
node_number=first_line.split()[0]
edge_number=int(first_line.split()[1])

t1=()
edges=[]
for i in range(edge_number):
            line=input()
            g_from=line.split()[0]
            g_to=line.split()[1]
            g_weight=int(line.split()[2])
            t1=(g_from,g_to,g_weight)
            edges.append(t1)


result=shortest_path(edges,edges[0][0],node_number)
if result==float("inf"):
    print ("1")
else:
   print(result[0])
    
