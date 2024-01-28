import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
graph = []
virus = []
q = deque()

blank_space = N * N

for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(N):
        if(line[j] == 2):
            virus.append([i, j])
            blank_space -= 1
        if(line[j] == 1):
            blank_space -= 1

comb = list(combinations(virus, M))

result = int(1e9)

for arr in comb:
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for x, y in arr:
        q.append([x, y, 0])
        visited[x][y] = 0
    max_time = 0
    cnt = 0
    while q:
        x, y, time = q.popleft()

        for i in move:
            dx = x + i[0]
            dy = y + i[1]

            if(dx < 0 or dy < 0 or dx >= N or dy >= N or visited[dx][dy] != -1):
                continue
            if(graph[dx][dy] == 1):
                continue
            if(graph[dx][dy] == 2):
                visited[dx][dy] = time+1
                q.append([dx, dy, time+1])
                continue
            visited[dx][dy] = time+1
            q.append([dx, dy, time+1])
            max_time = max(max_time, time+1)
            cnt += 1
    if(cnt == blank_space):
        result = min(result, max_time)
if(result == int(1e9)):
    print(-1)
else:
    print(result)