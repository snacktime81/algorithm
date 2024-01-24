import sys
from collections import deque


input = sys.stdin.readline
move=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

def bfs(graph, x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    
    while q:
        x, y = q.popleft()
        
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dx >= h or dy < 0 or dy >= w or visited[dx][dy] or graph[dx][dy] == 0):
                continue
            q.append([dx, dy])
            visited[dx][dy] = True
            cnt += 1
    return True

while True:
    w, h = map(int, input().split())
    if(w == 0 and h == 0):
        break
    graph = []

    for _ in range(h):
        line = list(map(int, input().split()))
        graph.append(line)

    result = 0
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if(not visited[i][j] and graph[i][j] == 1):
                bfs(graph, i, j, visited)
                result += 1
    print(result)
