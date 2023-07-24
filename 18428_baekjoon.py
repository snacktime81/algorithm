from itertools import combinations
from copy import deepcopy
from collections import deque

move = [(0,1), (0, -1), (1,0), (-1,0)]


def bfs(maps, x, y, visited):
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if( dx < 0 or dy < 0 or dx >= len(maps) or dy >= len(maps) or visited[dx][dy] == True):
                continue
            
            q.append((dx, dy))

            if(maps[x][y] == 'T'):
                for j in move:
                    dx = x
                    dy = y
                    while(True):

                        dx += j[0]
                        dy += j[1]

                        if( dx < 0 or dy < 0 or dx >= len(maps) or dy >= len(maps)):
                            break
                        if(maps[dx][dy] == 'O'):
                            break
                        if(maps[dx][dy] == 'S'):
                            return False
    return True
                        



n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(str, input().split())))

nums = []
for i in range(n):
    for j in range(n):
        nums.append((i, j))
                 
c = list(combinations(nums, 3))

boolean = True

for i in c:
    maps = deepcopy(graph)
    visited = [[False] * n for _ in range(n)]
    if(maps[i[0][0]][i[0][1]] != 'X' or maps[i[1][0]][i[1][1]] != 'X' or maps[i[2][0]][i[2][1]] != 'X'):
        continue
    
    for j in i:
        maps[j[0]][j[1]] = 'O'
    
    ch = bfs(maps, 0, 0, visited)
    if(ch):
        print("YES")
        boolean = False
        break


if(boolean):
    print('NO')
        