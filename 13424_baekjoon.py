import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


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


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    k = int(input())
    friends = list(map(int, input().split()))

    distance = []

    for friend in friends:
        d = dijk(friend, graph)
        distance.append(d)
    r = INF
    loc = 0

    for i in range(1, N+1):
        s = 0
        for d in distance:
            s += d[i]
        if(s < r):
            r = s
            loc = i
                
    print(loc)