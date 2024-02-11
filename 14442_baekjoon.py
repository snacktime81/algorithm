import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = int(1e9)

N, M, K = map(int, input().split())

graph = []

visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]

for i in range(N):
    line = input().rstrip()
    tmp = []
    for j in line:
        tmp.append(int(j))
    graph.append(tmp)

visited[0][0][0] = 1

q = deque([(0, 0, 0)])
answer = -1
while q:
    x, y, cnt = q.popleft()
    if x == N - 1 and y == M - 1:
        answer = visited[cnt][x][y]
        break

    for dx, dy in move:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 1 and cnt < K:
            if visited[cnt + 1][nx][ny] == 0:
                visited[cnt + 1][nx][ny] = visited[cnt][x][y] + 1
                q.append((nx, ny, cnt + 1))
        elif graph[nx][ny] == 0:
            if visited[cnt][nx][ny] == 0:
                visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                q.append((nx, ny, cnt))

print(answer)
