import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n = int(input())

visited = [ [ False for _ in range(n) ] for _ in range(n) ]

graph = []

move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for _ in range(n):
    line = list(input().strip())
    graph.append(line)
    
bGraph = deepcopy(graph)
bVisited = deepcopy(visited)

def common(graph, visited, x, y):
    
    d = deque([(x, y)])
    
    b = False
    
    if(visited[y][x]):
        return 0
    
    visited[y][x] = True
    
    while d:
        
        x, y = d.popleft()
        color = graph[y][x]

        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dy < 0 or dx >= n or dy >= n or visited[dy][dx]):
                continue
            
            if( graph[dy][dx] == color ):
                
                d.append([dx, dy])
                visited[dy][dx] = True
            
            
            
    return 1


def blind(graph, visited, x, y):
    
    d = deque([(x, y)])
    
    b = False
    
    if(visited[y][x]):
        return 0
    
    visited[y][x] = True
    
    while d:
        
        x, y = d.popleft()
        color = graph[y][x]
        

        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dy < 0 or dx >= n or dy >= n or visited[dy][dx]):
                continue
            
            if(( graph[dy][dx] == 'R' and graph[y][x] == 'G') or (graph[dy][dx] == 'G' and graph[y][x] == 'R')):
                d.append([dx, dy])
                visited[dy][dx] = True
                continue
            
            if( graph[dy][dx] == color ):
                
                d.append([dx, dy])
                visited[dy][dx] = True
            
            
            
    return 1

commonCnt = 0
blindCnt = 0

for i in range(n):
    for j in range(n):
        
        commonCnt += common(graph, visited, i, j) 
        blindCnt += blind(bGraph, bVisited, i, j)
        
print(commonCnt, blindCnt)
