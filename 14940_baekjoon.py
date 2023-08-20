from collections import deque
import sys

input = sys.stdin.readline



n, m = map(int, input().split())

graph = []
visited = [[False for _ in range(m)]  for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    graph.append(list(map(int, input().split())))


c = False
for i in range(n):
    for j in range(m):
        if( graph[i][j] == 2):
            x = i
            y = j
            c = True
            break
    if(c):
        break


q = deque([(x, y)])
graph[x][y] = 0
visited[x][y] = True

while q:
    x, y = q.popleft()
    
    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        
        if( dx < 0 or dy < 0 or dx >= n or dy >= m):
            continue
        
        if visited[dx][dy]:
            continue
        
        if(graph[dx][dy] == 0):
            continue
        
        graph[dx][dy] = graph[x][y] + 1
        q.append([dx, dy])
        visited[dx][dy] = True
    
    
for i in range(n):
    for j in range(m):
        if(visited[i][j] == False and graph[i][j] == 1):
            print(-1, end= ' ')
        else:
            print(graph[i][j], end= ' ')
    print()
    
    
    