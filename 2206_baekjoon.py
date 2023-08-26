from collections import deque
from copy import deepcopy, copy

n, m = map(int, input().split())

graph = []

for _ in range(n):
    arr = list(map(int, input()))
    graph.append(arr)
    
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

move = [(0,1), (1,0), (0, -1), (-1,0)]


def bfs(graph, visited):
    
    visited[0][0][0] = 1
    
    q = deque([(0,0,0)])
    
    while q:
        x, y, b = q.popleft()

        for i in move:
            dx = x + i[0]
            dy = y + i[1]

            if( dx < 0 or dx >= n or dy < 0 or dy >= m):
                continue


            if(graph[dx][dy] == 0 and visited[dx][dy][b] == 0):
                q.append([dx, dy, b])
                visited[dx][dy][b] = visited[x][y][b] + 1
            
            if(graph[dx][dy] == 1 and b == 0):
                q.append([dx, dy, 1])
                visited[dx][dy][1] = visited[x][y][0] + 1
    
    if(visited[n-1][m-1][b] == 0):
        return -1
    else:
        return visited[n-1][m-1][b]



print(bfs(deepcopy(graph), deepcopy(visited)))