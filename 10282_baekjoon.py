import sys
input = sys.stdin.readline
from heapq import heappop, heappush
INF = int(1e9)
    
def dijk(start, distance):
    q= []

    heappush(q, (0, start))
    while q:
        dist, now = heappop(q)
        if(distance[now] < dist):
            continue
        for i in computer[now]:
            cost = i[1] + dist
            
            if(cost < distance[i[0]]):
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

                

    
T = int(input())


for _ in range(T):
    n,d,c = map(int, input().split())
    
    parent = [i for i in range(n+1)]
    computer = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    for _ in range(d):
        a,b,s = map(int, input().split())
        computer[b].append([a,s])
    distance[c] = 0
    dijk(c, distance)
    
    mc = 0
    cnt = 0
    
    for i in distance:
        if(i == INF):
            continue
        else:
            mc = max(mc, i)
            cnt += 1
    
    print(cnt, (mc))