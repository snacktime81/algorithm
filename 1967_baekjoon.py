import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)

def dijk(graph, start):
    distance = [INF for _ in range(n+1)]
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if(distance[now] < dist):
            continue
            
        for i in graph[now]:
            cost = i[1] + dist
            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance
n = int(input())
graph = [[] for _ in range(n+1)]
pick = 0 # +1 부터 리프노드


for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    pick = a


r = 0


d = dijk(graph, 1)

index = 1
for i in range(1, n+1):
    if(d[i] > d[index]):
        index = i

# for i in range(pick+1, n+1):
#     d = dijk(graph, i, depend)
#     rd(graph, i)
#     for dist in d:
#         if(dist != INF):
#             r = max(r, dist)
d = dijk(graph, index)
r = max(d[1:])
print(r)
    
    