import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
graph = []


move = [(1,0), (-1,0),(0,1),(0,-1)]

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

def check(x, y, visited):
    global graph
    q = deque([(x,y)])
    tmp = [[0] * m for _ in range(n)]
    
    coor = []
    
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        #print(x, y)
        coor.append([x,y])

        cnt = 0
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx<0 or dy<0 or dx>=n or dy>=m):
                continue
            if(graph[dx][dy] == 0):
                cnt += 1
                continue
            if not visited[dx][dy]:
                visited[dx][dy] = True
                q.append([dx, dy])
        #print(graph[x][y], cnt)
        if(graph[x][y] - cnt >= 0):
            tmp[x][y] = graph[x][y] - cnt
        else:
            tmp[x][y] = 0
    
    for x, y in coor:
        graph[x][y] = tmp[x][y]
    return 1

            
time = 0

while True:
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    c = False
    for i in range(n):
        for j in range(m):
            if(graph[i][j] != 0 and visited[i][j] == False):
                cnt += check(i, j, visited)
                if(cnt > 2):
                    c = True
                    break
        if(c):
            break
    # print(cnt)
    #print(graph)
    if(cnt > 1):
        print(time)
        break
    elif(cnt == 0):
        print(0)
        break
    time+=1