import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

start = int(input())

INF = int(1e9)

weight = [ INF for _ in range(n+1)]

graph = [ [] for _ in range(n+1) ]



for _ in range(m):
    toNode, fromNode, wei = map(int, input().split())
    graph[toNode].append((fromNode, wei))
    

def dij(start):
    q = []
    
    heapq.heappush(q, (0, start))

    weight[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if( weight[now] < dist):
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if( cost < weight[i[0]]):
                weight[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dij(start)
cnt = True

for i in weight:
    if(cnt):
        cnt = False
        continue
    if i == INF:
        print("INF")
    else:
        print(i)