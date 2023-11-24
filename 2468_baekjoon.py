# https://www.acmicpc.net/problem/2468

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n = int(input())

graph = []

move = [(1,0), (-1,0), (0,1), (0,-1)]

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

visited = []

def bfs(graph, height, x, y):

    if(graph[x][y] <= height):
        return False

    que = deque([(x,y)])
    graph[x][y] = height

    while que:
        (x, y) = que.popleft()

        for i in move:
            dx = x + i[0]
            dy = y + i[1]

            if( dx < 0 or dy < 0 or dx >= n or dy >= n):
                continue
            if(graph[dx][dy] <= height):
                continue
            
            graph[dx][dy] = height
            que.append((dx, dy))
    return True

maxCnt = 0

for i in range(101):
    cnt = 0
    graph_tmp = deepcopy(graph)
    for k in range(n):
        for l in range(n):
            if(bfs(graph_tmp,i,k,l)):
                cnt += 1
    if(cnt > maxCnt):
        maxCnt = cnt

print(maxCnt)