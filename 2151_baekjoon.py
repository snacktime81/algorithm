import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e9)


def dfs(graph, x, y, mirror, direction):
    
    if(visited[x][y][direction] < mirror):
        return 0
    block = graph[x][y]

    cost = visited[x][y][direction]
    visited[x][y][direction] = min(cost, mirror)
    
    if(block == '!'):
        for i in move:
            if(i[2]  == illegalMove[direction]):
                continue
            
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dy < 0 or dx >= n or dy >= n):
                continue
            if(graph[dx][dy] == '*'):
                continue
            
            if(i[2] == direction):
                new = mirror
            else:
                new = mirror+1
            
            dfs(graph,dx,dy,new,i[2])
            #graph[dx][dy] = block
    else: # . 일때
        for i in move:
            if(i[2] != direction):
                continue
            
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dy < 0 or dx >= n or dy >= n):
                continue
            if(graph[dx][dy] == '*'):
                continue
            
            dfs(graph, dx, dy, mirror, direction)
            #graph[dx][dy] = block

            

n = int(input())
graph = []
points = []
visited = [[[INF, INF, INF, INF]]*n for _ in range(n)] 
#print(visited)
for i in range(n):
    line = list(input().rstrip())
    graph.append(line)
    
    if ('#' in line):
        for j in range(n):
            if(line[j] == '#'):
                points.append([i,j])

move = [[1,0,0], [-1, 0, 1], [0, 1, 2], [0, -1, 3]]
directionNum = {'down': 0, 'up':1, 'right':2, 'left':3}



sx, sy = points[0]
ex, ey = points[1]

cost = int(1e9)

illegalMove = {0:1, 1:0, 2:3, 3:2}

for i in move:
    x = sx + i[0]
    y = sy + i[1]
    if(x < 0 or y < 0 or x >= n or y >= n):
        continue
    if(graph[x][y] == '*'):
        continue
    #print(x,y,i[2])
    dfs(graph,x,y,0,i[2])

    
for k in range(4):
    for i in visited:
        for j in i:
            if(j[k] == INF):
                print('*', end='')
            else:
                print(j[k], end='')
        print()
    print()



print(visited[ex][ey])