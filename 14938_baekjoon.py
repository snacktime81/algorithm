import sys
from heapq import heappop, heappush


input = sys.stdin.readline
INF = int(1e9)
n, m, r = map(int ,input().split())

inp = list(map(int,input().split()))
site = [0] + inp

#print(site)


graph = [[] for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int ,input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])
    
#distance = [INF] * (n+1)
def dijk(s):
    distance = [INF] * (n+1)
    q = []
    heappush(q,(0, s))
    distance[s] = 0
    
    while q:
        dist, now = heappop(q)
        if(distance[now] < dist):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if(cost < distance[i[0]]):
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance

mR = 0
for i in range(1, n+1):
    tmp = dijk(i)
    result = 0
    for j in range(1, n+1):
        if(tmp[j] <= m):
            result += site[j]
    if(mR < result):
        mR = result
print(mR)
    