import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N = int(input())
graph = []

for _ in range(N):
    line = input().rstrip()
    arr = []
    for i in line:
        arr.append(int(i))
    graph.append(arr)
    

q = deque([(0, 0, 0)])  # x, y, black
visited = [[INF] * N for _ in range(N)]
visited[0][0] = 0

while q:
    x, y, black = q.popleft()
    
    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        
        if(dx < 0 or dx >= N or dy < 0 or dy >= N):
            continue

        room = graph[dx][dy]
        dblack = black if room else black+1
        
        if(visited[dx][dy] > dblack):
            q.append([dx, dy, dblack])
            visited[dx][dy] = dblack
print(visited[-1][-1])