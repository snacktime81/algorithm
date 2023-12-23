# https://www.acmicpc.net/problem/2146

import sys
from collections import deque

input = sys.stdin.readline

move =[(-1,0), (1,0), (0,1), (0,-1)]

graph = []

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    
visited = [[0] * n for _ in range(n)]
def bfs(x, y, cnt, visited):
    
    if(visited[x][y]):
        return 0
    q = deque([(x, y)])
    visited[x][y] = True
    graph[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if( dx < 0 or dy < 0 or dx >= n or dy >= n or visited[dx][dy] or graph[dx][dy] == 0):
                continue
            graph[dx][dy] = cnt
            visited[dx][dy] = True
            q.append([dx, dy])
cnt = 1
for i in range(n):
    for j in range(n):
        if( not visited[i][j] and graph[i][j] != 0):
            bfs(i, j , cnt , visited)
            cnt += 1

def search(num):
    q = deque()
    
    distance = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == num):
                q.append([i,j])
    
    while q:
        x, y = q.popleft()
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if( dx < 0 or dy < 0 or dx >= n or dy >= n):
                continue
            
            if(graph[dx][dy] != num and graph[dx][dy] != 0):
                return distance[x][y]
            
            if(distance[dx][dy] > distance[x][y] + 1 or (distance[dx][dy] == 0 and graph[dx][dy] != num)):
                distance[dx][dy] = distance[x][y] + 1
                q.append([dx, dy])
            
r = int(1e9)
for i in range(1, cnt):
    r = min(r, search(i))
print(r)