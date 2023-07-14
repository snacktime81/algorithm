import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

all = []

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            all.append((i,j))
allC = list(combinations(all, 3))


def bfs(graph, start):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([start])
    cnt = 0
    
    x, y = start
    
    if(graph[x][y] != 2):
        return False
    
    while q:
        x, y = q.popleft()
        if(graph[x][y] == 2):
            cnt += 1
            graph[x][y] = 3
            for i in move:
                dx = x + i[0]
                dy = y + i[1]
                
                if(dx < 0 or dy < 0 or dx >= n or dy >= m):
                    continue

                    
                if(graph[dx][dy] == 0 or graph[dx][dy] == 2):
                    q.append((dx, dy))
                    graph[dx][dy] = 2
                    #print(dx,dy)
                    
                
    return cnt


maximum = 0
for k in allC:
    r = 0
    tmpGraph = copy.deepcopy(graph)
    x1, y1 = k[0]
    x2, y2 = k[1]
    x3, y3 = k[2]
    tmpGraph[x1][y1] = 1
    tmpGraph[x2][y2] = 1
    tmpGraph[x3][y3] = 1
    for i in range(n):
        for j in range(m):
            v = bfs(tmpGraph, (i, j))
            
    
    for i in range(n):
        for j in range(m):
            if(tmpGraph[i][j] == 0):
                r+=1
    if(r > maximum):
        maximum = r
print(maximum)


# 49 - 12 = 37

