import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int ,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

ts, tx, ty = map(int, input().split())
    
move = [(0,1), (0, -1), (-1, 0), ( 1, 0)]

data = []

for i in range(n):
    for j in range(n):
        if(graph[i][j] != 0):
            data.append([graph[i][j], i, j, 0])
            
data.sort(key=lambda x:x[0])


q = deque()

for i in data:
    q.append(i)
            
while q:
    virus, x, y, s = q.popleft()
    
    if(s == ts):
        break
    
    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        if(dx < 0 or dy < 0 or dx >= n or dy >= n or graph[dx][dy] != 0):
            continue
        if(graph[dx][dy] == 0):
            graph[dx][dy] = virus
            q.append([virus, dx, dy, s+1])

print(graph[tx-1][ty-1])