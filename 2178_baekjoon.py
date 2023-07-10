import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []

move = [(0,1), (0, -1), (1, 0), (-1, 0)]
visited = []
for i in range(n):
    line = list(input().rstrip())
    maps.append(list(map(int, line)))
    visited.append([False] * m)
def bfs(maps, start):
    queue = deque([start])
    
    while queue:
        
        x, y = queue.popleft()        
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            #print(dx,dy)
            #print(visited)
            if(dx < 0 or dx >= n or dy < 0 or dy >= m):
                continue

            if(maps[dx][dy] == 0):
                continue

            if not visited[dx][dy]:
                #print(dx, dy)
                queue.append((dx,dy))
                visited[dx][dy] = True
                maps[dx][dy] += maps[x][y]
        

bfs(maps, (0,0))

print(maps[n-1][m-1])