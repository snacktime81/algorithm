import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijk(gr):
    start = 1
    distance = [INF] * (N+1)
    distance[1] = 0
    q = []
    heappush(q, [0, 1])

    while q:
        dist, node = heappop(q)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(q, [cost, i[0]])
    return distance[N]

print(dijk(graph))
