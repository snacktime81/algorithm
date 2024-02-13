import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def dijk(start):
    distance = [INF] * (N+1)
    visited = [0] * (N+1)
    visited[start] = start
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(distance[i[0]] > cost):
                if visited[now] != start:
                    visited[i[0]] = visited[now]
                else:
                    visited[i[0]] = i[0]
                
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return visited


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

result = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    visited = dijk(i)
    
    for j in range(1, N+1):
        node = visited[j]
        if(j != i):
            result[i][j] = node
    
    
for i in range(1, N+1):
    for j in range(1, N+1):
        if(i == j):
            print('-', end=' ')
        else:
            print(result[i][j], end=' ')
    print()