import sys
from collections import deque

input = sys.stdin.readline
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 서 북 동 남

N, M = map(int, input().split())
graph = []

for _ in range(M):
    line = list(map(int, input().split()))
    graph.append(line)

    
visited = [[False] * N for _ in range(M)]

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    size = 1
    
    poses = [[x, y]]
    
    while q:
        x, y = q.popleft()
        num = graph[x][y]
        for i in range(3, -1, -1):
            if(num - 2**i >= 0):
                num -= 2 ** i
                continue
            
            dx = x + move[i][0]
            dy = y + move[i][1]
            if(dx < 0 or dx >= M or dy < 0 or dy >= N or visited[dx][dy]):
                continue
            
            q.append([dx, dy])
            visited[dx][dy] = True
            size += 1
            poses.append([dx, dy])
    for x,y in poses:
        visited[x][y] = size
    return size


        
cnt = 0
size = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            size = max(size, bfs(i, j, visited))

def bfs2(x, y, visited):
    q = deque([(x, y, 0)])
    size = visited[x][y]
    visited[x][y] = False
    result = 0
    costs = [[False] * N for _ in range(M)]
    while q:
        x, y, c = q.popleft()
        num = graph[x][y]
        if(c == 1):
            continue
        for i in range(3, -1, -1):
            if(num - 2**i >= 0):
                num -= 2**i
                if(c == 0):
                    dx = x + move[i][0]
                    dy = y + move[i][1]
                    if(dx < 0 or dx >= M or dy < 0 or dy >= N or not visited[dx][dy]):
                        continue
                    costs[dx][dy] = visited[dx][dy] 
                    q.append([dx, dy, c+1])
                    
            else:
                dx = x + move[i][0]
                dy = y + move[i][1]
                if(dx < 0 or dx >= M or dy < 0 or dy >= N or not visited[dx][dy]):
                        continue
                visited[dx][dy] = False
                q.append([dx, dy, c])
                costs[dx][dy] = False
                
    for i in costs:
        result = max(result, size+max(i))
    return result

result = 0
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            result = max(result, bfs2(i, j, visited))
print(cnt)
print(size)
print(result)