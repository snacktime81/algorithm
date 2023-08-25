from collections import deque

m, n = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))
    
start = (0, 0)

ex = m-1
ey = n-1

move = [(0,1),(0,-1),(1,0),(-1,0)]

cnt = 0

x, y = start

q = deque([(x, y)])

while q:
    x, y = q.popleft()
    
    if( x == ex and y == ey):
        cnt += 1
        continue
    
    num = graph[x][y]
    
    for i in move:
        
        dx = x + i[0]
        dy = y + i[1]
        
        if( dx < 0 or dy < 0 or dx >= m or dy >= n):
            continue
        
        if( graph[dx][dy] < num):
            q.append([dx,dy])
            
print(cnt)
        