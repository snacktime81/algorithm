import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)
def dijk(start, end):
    q = []
    heappush(q, (0, start))
    distance = [INF for _ in range(n+1)]
    
    while q:
        dist, now = heappop(q)
        if(distance[now] < dist):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if( cost < distance[i[0]]):
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
                
    return distance[end]
            


n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
v1, v2 = map(int ,input().split())

a1 = dijk(1, v1)
a2 = dijk(v1, v2)
a3 = dijk(v2, n)
dist = a1 + a2 + a3 # 무조건 초기화 불가능 하면 밑에 줄에서 -1로 초기화 해준다
if(a1 == INF or a2 == INF or a3 == INF): # 불가능 하면 -1로 초기화
    dist = -1
else:
    b1 = dijk(1, v2)
    b2 = dijk(v2, v1)
    b3 = dijk(v1, n)
    if(b1 == INF or b2 == INF or b3 == INF):
        dist = max(dist, -1)
    else:
        dist = min(dist, b1+b2+b3)
if(v1 == 1 and v2 == n):        
    c1 = dijk(v1, v2)
    if(c1 != INF):
        dist = min(c1, dist)
print(dist)