#18352 

import sys
import heapq

input = sys.stdin.readline


n,m,k,x = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1,b))



def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if(distance[now] < dist):
            continue
    
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance    

distance = dijkstra(graph, x, distance)
#print(distance)
check = True

city = []

for i in range(len(distance)):
    if(distance[i] == k):
        print(i)
        check = False


if(check):
    print(-1)