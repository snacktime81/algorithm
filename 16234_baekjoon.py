import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int, input().split())

graph = []

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    
def bfs(graph,x,y,site, cnt):
    q = deque([(x, y)])
    site[x][y] = cnt
    pos = [[x,y]]
    s = graph[x][y]
    while q:
        x, y = q.popleft()
        p = graph[x][y]
        
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if(dx < 0 or dy < 0 or dx >= n or dy >= n):
                continue
            if(site[dx][dy]):
                continue
            
            if(l <= abs(p-graph[dx][dy]) <= r):
                site[dx][dy] = cnt
                q.append([dx, dy])
                pos.append([dx,dy])
                s+=graph[dx][dy]
                
    return pos, s
check = True
result = 0
move = [(0,1), (0,-1), (1,0), (-1,0)]
while True:
    result += 1
    site = [[0 for _ in range(n)]  for _ in range(n)]
    cnt = 1
    # 국경 개방
    for i in range(n):
        for j in range(n):
            if(not site[i][j]):
                pos, s = bfs(graph,i,j,site,cnt)
                avg = s//len(pos)
                for x, y in pos:
                    graph[x][y] = avg
                cnt += 1
    
    # for i in site:
    #     print(i)
    # print()
    if(cnt-1 == n*n):
        print(result-1)
        break