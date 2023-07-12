import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start, distance):
    que = deque([start])
    
    distance[start] = 0
    
    while que:
        v = que.popleft()
        for i in graph[v]:
            if(distance[i] == int(1e9)):
                distance[i] = distance[v] + 1
                que.append(i)
    return distance

distance = bfs(graph, x, distance)

check = True
for i in range(len(distance)):
    if(distance[i] == k):
        print(i)
        check = False

if(check):
    print(-1)