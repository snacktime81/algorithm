# https://www.acmicpc.net/problem/11779

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append([b, c])
    
f, to = map(int, input().split()) # 출발, 도착

distance = [INF] * (n+1)
parent = [i for i in range(n+1)]
q = []

heappush(q, (0, f))

while q:
    dist, now = heappop(q)
    if(distance[now] < dist):
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if(distance[i[0]] > cost):
            distance[i[0]] = cost
            heappush(q, (cost, i[0]))
            parent[i[0]] = now
            
cnt = 0
l = []
cost = distance[to]
# print(parent)
# print(distance)
while True:
    l.append(to)
    to = parent[to]
    cnt += 1
    if(f == to):
        cnt += 1
        l.append(f)
        break

l2 = []

for i in range(len(l)-1, -1, -1):
    l2.append(l[i])

print(cost)
print(cnt)
for i in l2:
    print(i, end=' ')