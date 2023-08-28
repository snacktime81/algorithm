import sys
from heapq import heappush, heappop


input = sys.stdin.readline
INF = int(1e9)


T = int(input())


def dij(num, start):
    q = []
    
    heappush(q, (num, start))

    distance = [ INF for _ in range(n+1)]
    distance[start] = num
    
    while q:

        dist, now = heappop(q)
    
        if(dist > distance[now]):
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if( cost < distance[i[0]]):
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance
            
    
    
for _ in range(T):
    
    n, m, t = map(int, input().split())
    
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]

    fromNode = []
    
    for _ in range(m):
        a, b, d = map(int, input().split())
            
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        fromNode.append(int(input()))

    d0 = dij(0, s)
    dg = dij(0, g)
    dh = dij(0, h)
    
    fromNode.sort()
    
    for i in fromNode:
        wayG = d0[g] + dg[h] + dh[i] 
        wayH = d0[h] + dh[g] + dg[i]
        
        if( wayG == d0[i] or wayH == d0[i]):
            print(i, end=' ')
    print()