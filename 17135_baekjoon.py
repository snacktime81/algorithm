# https://www.acmicpc.net/problem/17135

import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n,m,d = map(int, input().split())

graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    
def move_map(graph):
    line = [[0]*m]
    graph.pop();
    for i in graph:
        line.append(i)
    return line


pos = []
for i in range(m):
    pos.append([n-1, i])

archers = list(combinations(pos, 3)) # 궁사가 쏜 첫발의 위치
move = [(0,-1), (-1,0), (0,1)]

r = 0

def bfs(graph, x, y):
    visited = [[0] * m for _ in range(n)]

    if(graph[x][y] == 1):
        return (x,y)
    q = deque([(x,y,1)])
    visited[x][y] = True
    dist = 1
    while q:
        x, y, dist = q.popleft()
        if(dist >= d):
            continue
        for i in move:
            dx = x + i[0]
            dy = y + i[1]

            if(dist > d):
                continue
            if(dx < 0 or dy < 0 or dx >= n or dy >= m):
                continue
            if(visited[dx][dy]):
                continue
            if(graph[dx][dy] == 1):
                return (dx, dy)
            q.append([dx,dy,dist+1])
            visited[dx][dy] = True
    return (-1, -1)

r = 0
for a, b, c in archers:
    cnt = 0
    tmp = deepcopy(graph)
    for _ in range(n):
        x1, y1 = bfs(tmp, a[0], a[1])
        x2, y2 = bfs(tmp, b[0], b[1])
        x3, y3 = bfs(tmp, c[0], c[1])

        if(tmp[x1][y1] == 1 and x1 != -1):
            cnt += 1
            tmp[x1][y1] = 0 # 같은 적을 쏠 수 있기 때문
        if(tmp[x2][y2] == 1 and x2 != -1):
            cnt += 1
            tmp[x2][y2] = 0
        if(tmp[x3][y3] == 1 and x3 != -1):
            cnt += 1
            tmp[x3][y3] = 0
        
        
        # for i in tmp:
        #     print(i)
        # print()
        tmp = move_map(tmp)

    r = max(r,cnt)
print(r)