import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
k_move = [(-1, -2), (-2, -1), (2, 1), (1, 2), (1, -2), (2, -1), (-2, 1), (-1, 2)]

K = int(input())
W, H = map(int, input().split())

g = []

for _ in range(H):
    line = list(map(int, input().split()))
    g.append(line)

q = deque([(0, 0, 0)])  # x, y, knight_cnt, total_move

visited = [[[INF] * W for _ in range(H)] for _ in range(K+1)]
visited[0][0][0] = 0

while q:
    x, y, k_cnt = q.popleft()

    for i in move:
        dx = x + i[0]
        dy = y + i[1]

        if dx < 0 or dx >= H or dy < 0 or dy >= W or g[dx][dy] == 1:
            continue

        if visited[k_cnt][dx][dy] > visited[k_cnt][x][y] + 1:
            visited[k_cnt][dx][dy] = visited[k_cnt][x][y] + 1
            q.append([dx, dy, k_cnt])

    if k_cnt < K:
        for i in k_move:
            dx = x + i[0]
            dy = y + i[1]

            if dx < 0 or dx >= H or dy < 0 or dy >= W or g[dx][dy] == 1:
                continue

            if visited[k_cnt+1][dx][dy] > visited[k_cnt][x][y] + 1:
                visited[k_cnt+1][dx][dy] = visited[k_cnt][x][y] + 1
                q.append([dx, dy, k_cnt+1])

result = INF

for i in visited:
    if i[-1][-1] != INF:
        result = min(i[-1][-1], result)

if result == INF:
    print(-1)
else:
    print(result)