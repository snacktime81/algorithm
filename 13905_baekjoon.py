import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n,m = map(int, input().split())
s,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c= map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
distance = [0] * (n+1)

q = deque([(INF, s)])
distance[s] = INF
while q:
    dist, now = q.popleft()
    if(now == e):
        continue
    if(distance[now] > dist):
        continue
    for i in graph[now]:
        w = min(dist, i[1])
        if (distance[i[0]] < w):
            distance[i[0]] = w
            q.append([w,i[0]])
print(distance[e])