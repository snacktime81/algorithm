import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


''' 
아이디어:
그래프를 오른쪽으로 90도 회전시키고 
원본 그래프의 끝점에
회전시킨 그래프를 붙힌다.
'''

n = int(input())
graph = [[0 for _ in range(101)] for _ in range(101)]
move = [(0,1), (-1,0), (0,-1), (1,0)]


def turn(graph, x, y): # 그래프, 끝점 그래프를 오른쪽으로 90도 회전
    tmp = [[0 for _ in range(101)] for _ in range(101)]
    
    for i in range(101):
        for j in range(101):
            if(graph[i][j] == 1):
                tmp[j][100-i] = graph[i][j]
    
    return [tmp, y, 100-x]


for _ in range(n): 
    y, x, d, g = map(int, input().split()) # 시작좌표, 방향, 세대
    
    tmpGraph = [[0 for _ in range(101)] for _ in range(101)]
    
    ex, ey = x + move[d][0], y + move[d][1] # 1세대
    tmpGraph[x][y] = 1
    tmpGraph[ex][ey] = 1
    
    for _ in range(g):
        tmp, nx, ny = turn(tmpGraph, ex, ey) # nx, ny는 오른쪽으로 돌린 그래프의 시작점
        dx = ex - nx # 회전한 그래프의 시작점을 원본 그래프의 끝점에 붙혀야 함으로, nx + dx = ex 즉 그래프를 회전 시켰기 때문에 좌표값이 일정하게 차이가 나고 그 차이값이 dx,dy 이다.
        dy = ey - ny
        #print('dx, dy: ', dx, dy)
        for i in range(101):
            for j in range(101):
                if(tmp[i][j] == 1):
                    #print(i,j)
                    tmpGraph[i + dx][j + dy] = 1
        ex, ey = y+dx, 100-x+dy # 결국 마지막 지점은 시작 좌표가 회전한 값이다. (중요)
        print('ex ', ex,ey)
    for i in range(101):
        for j in range(101):
            if(tmpGraph[i][j] == 1):
                print('i,j: ', i, j)
                graph[i][j] = 1
    #print()
    
    
cnt = 0        
for i in range(100):
    for j in range(100):
        ax, ay = i + 1, j + 1
        bx, by = i, j + 1
        cx, cy = i + 1, j
        if(graph[i][j] == 1 and graph[ax][ay] == 1 and graph[bx][by] == 1 and graph[cx][cy] == 1):
            cnt += 1
            
print(cnt)