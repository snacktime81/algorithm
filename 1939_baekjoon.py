import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])


distance = [0 for _ in range(n+1)]
start, end = map(int, input().split())
q = []


heappush(q, (0, start))

while q:
    dist ,now = heappop(q)
    dist = -dist
    #print(now)
    if(distance[now] > dist ): # 최대힙을 써서 최대한 스킵
        continue
    for i in graph[now]:
        if(dist == 0):
            if(distance[i[1]] <= i[0]):
                distance[i[1]] = i[0]
                heappush(q, (-i[0], i[1]))
        else:
            cost = min(dist, i[0])

            if(cost > distance[i[1]]):
                distance[i[1]] = cost
                heappush(q, (-cost, i[1]))

print(distance[end])