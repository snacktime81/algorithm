import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def find(x):
    if(parent[x] != x):
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

        
def dijk(start, graph):
    q = []
    distance = [INF] * (N+1)
    heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heappop(q)

        if(distance[now] < dist):
            continue

        for node, w in graph[now]:
            cost = dist + w

            if(distance[node] > cost):
                heappush(q, (cost, node))
                distance[node] = cost
    return distance
    
    
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
group = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
    graph[a].append([b, 1])
    graph[b].append([a, 1])
    
for i in range(1, N+1):
    tmp = find(i)
    group[tmp].append(i)
    
result = []
cnt = 0

for arr in group:
    if(len(arr) == 0):
        continue

    cnt += 1
    r = INF
    index = -1
    
    for i in arr:
        d = dijk(i, graph)
        
        m = -1
        for j in d:
            if(j != INF and j > m):
                m = j
        if(r > m):
            r = m
            index = i
    result.append(index)
result.sort()
print(cnt)
for i in result:
    print(i)