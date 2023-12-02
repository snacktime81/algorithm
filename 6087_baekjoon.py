import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e8)

w, h = map(int, input().split())

graph = []

for _ in range(h):
    line = list(input().rstrip())
    graph.append(line)

points = []
    
for i in range(h):
    for j in range(w):
        if(graph[i][j] == 'C'):
            points.append([i, j])

sx, sy = points[0]
ex, ey = points[1]

visited = [ [[INF, INF, INF, INF] for _ in range(w)] for _ in range(h) ] # 각 방향별로 거울 사용 횟수를 저장

move = [[1, 0, 0], [-1, 0, 1], [0, 1, 2], [0,-1, 3]]
illegalMove = {1:0, 0:1, 2:3, 3:2}

def bfs(sx,sy, d):
    q = deque([(0, sx, sy, d)]) # curve, x, y , direction
    visited[sx][sy][d] = 0
    while q:
        
        curve, x, y, d = q.popleft()

        if(x == ex and y == ey):
            visited[ex][ey][d] = curve
            continue

        for i in move:
            if(i[2] == illegalMove[d]): # 180도 회전은 불가하다
                continue
            dx = x + i[0]
            dy = y + i[1]

            if(dx < 0 or dy < 0 or dx >= h or dy >= w):
                continue
            if(graph[dx][dy] == '*'):
                continue
                
            if(i[2] == d and visited[dx][dy][d] < curve):
                continue
            elif(visited[dx][dy][i[2]] < curve + 1):
                continue

            if(i[2] == d): # 직진중
                q.append([curve, dx, dy, d])
                visited[dx][dy][d] = curve
            else: # 거울 설치
                q.append([curve+1, dx, dy, i[2]])
                visited[dx][dy][i[2]] = curve+1
            

                
for i in move: # 출발 좌표에서 상하좌우 4방향은 거울 사용횟수가 0회
    x = sx + i[0]
    y = sy + i[1]
    #print(x,y,i[2])
    if(x < 0 or y < 0 or x >= h or y >= w):
        continue
    if(graph[x][y] == '*'):
        continue
    bfs(x, y , i[2])
print(min(visited[ex][ey]))
