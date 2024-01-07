# 1000log1000 = 3000  3000*1000=3000000 3백만
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)


def dijk(start):
    q = []
    distance = [INF] * (n+1)
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(distance[i[0]] > cost):
                heappush(q, (cost, i[0]))
                distance[i[0]] = cost
    return distance


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


for _ in range(m):
    a, b = map(int, input().split())
    print(dijk(a)[b])

