import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(100)] for _ in range(100)]
move = [(0,1), (-1,0), (0,-1), (1,0)]


def turn(graph, x, y): # 그래프, 끝점
    tmp = [[0 for _ in range(100)] for _ in range(100)]
    
    for i in range(100):
        for j in range(100):
            if(graph[i][j] == 1):
                tmp[j][99-i] = graph[i][j]
    
    return [tmp, y, 99-x]


def findEdge(x, y, graph):
    q = deque([(x, y)])
    graph[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dy < 0 or dx >= 100 or dy >= 100):
                continue
            if(graph[dx][dy] == 0):
                continue
            
            q.append([dx, dy])
            graph[dx][dy] = 0
    return x, y
            
                
    

for _ in range(n):
    y, x, d, g = map(int, input().split()) # 시작좌표, 방향, 세대
    
    tmpGraph = [[0 for _ in range(100)] for _ in range(100)]
    
    ex, ey = x + move[d][0], y + move[d][1]
    tmpGraph[x][y] = 1
    tmpGraph[ex][ey] = 1
    
    for _ in range(g):
        tmp, nx, ny = turn(tmpGraph, ex, ey)
        dx = ex - nx
        dy = ey - ny
        #print('dx, dy: ', dx, dy)
        for i in range(100):
            for j in range(100):
                if(tmp[i][j] == 1):
                    #print(i,j)
                    tmpGraph[i + dx][j + dy] = 1
        ex, ey = findEdge(x, y, deepcopy(tmpGraph))
    for i in range(100):
        for j in range(100):
            if(tmpGraph[i][j] == 1):
                graph[i][j] = 1
    
    
    # for i in range(100):
    #     for j in range(100):
    #         print(graph[i][j], end='')
    #     print()

    
cnt = 0        
for i in range(99):
    for j in range(99):
        ax, ay = i + 1, j + 1
        bx, by = i, j + 1
        cx, cy = i + 1, j
        if(graph[i][j] == 1 and graph[ax][ay] == 1 and graph[bx][by] == 1 and graph[cx][cy] == 1):
            cnt += 1
            
print(cnt)