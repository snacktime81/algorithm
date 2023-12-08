import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
x, y = (0, 0)
ex = n-1
ey = m-1

move = [(0,1),(0,-1),(1,0),(-1,0)]




visited = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(x, y):
    if(x == ex and y == ey):
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0
    
    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        
        if(dx < 0 or dy < 0 or dx >= n or dy >= m):
            continue
        if(graph[x][y] <= graph[dx][dy]):
            continue
            
        visited[x][y] += dfs(dx, dy)
        #print(visited)
    
    return visited[x][y]

cnt = dfs(x, y)   

for i in visited:
    print(i)
print(cnt)
        