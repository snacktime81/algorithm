import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)


def bfs(graph, x, y, direction):
    q = deque([(x, y, 0, direction)])
    
    while q:
        x, y, new, direction = q.popleft()
        block = graph[x][y]
        #print('x, y: ', x, y, visited[2][1][3], )
        if(visited[x][y][direction] > new):
            visited[x][y][direction] = new
        else:
            continue
        #print('x, y,   cost, new: ', x, y, visited[x][y][direction], new)
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
                
                if(i[2] == direction): #거울설치 안함
                    q.append([dx, dy, new, direction])
                else: #거울 설치
                    q.append([dx, dy, new+1, i[2]])
                    
                
        else: # . 일때
            #graph[x][y] = '*'
            dx = x + move[direction][0]
            dy = y + move[direction][1]

            if(dx < 0 or dy < 0 or dx >= n or dy >= n):
                continue
            if(graph[dx][dy] == '*'):
                continue
            q.append([dx,dy,new,direction])
        #print('x, y: ', x, y, visited )
    
n = int(input())
graph = []
points = []

visited = [ [[INF, INF, INF, INF] for _ in range(n)] for _ in range(n)] 
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
    bfs(graph,x,y,i[2])
    
print(min(visited[ex][ey]))