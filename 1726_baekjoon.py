import sys
from collections import deque

input = sys.stdin.readline
move = {3: (1, 0), 4: (-1, 0), 2: (0, -1), 1: (0, 1)}
reverse = {1:2, 2:1, 3:4, 4:3}
INF = int(1e9)

M, N = map(int, input().split())

g = []
for _ in range(M):
    line = list(map(int, input().split()))
    g.append(line)
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())



visited = [[[INF]*N for _ in range(M)] for _ in range(5)]
q = deque([(sx-1, sy-1, sd)])
visited[sd][sx-1][sy-1] = 0

while q:
    x, y, d = q.popleft()
    #print(x, y, d)
    if x == ex-1 and y == ey-1:
        #print(x, y, d)
        if d == ed:
            break
        else:
            if reverse[d] != ed:
                if visited[ed][x][y] > visited[d][x][y] + 1:
                    visited[ed][x][y] = visited[d][x][y] + 1
                else:
                    visited[ed][x][y] = min(visited[ed][x][y], visited[d][x][y] + 1)
            else:
                if visited[ed][x][y] > visited[d][x][y] + 2:
                    visited[ed][x][y] = visited[d][x][y] + 2
                else:
                    visited[ed][x][y] = min(visited[ed][x][y], visited[d][x][y] + 2)

    check = True  # 이게 핵심  밑에 코드에서 1, 2, 3칸을 건너 뛸 수 있으므로 0 1 0 과 같은 상황에서도 3번째 칸으로 넘어갈 수 있는 로직의 문제점을 막아준다.
    for i in range(1, 4):
        dx = x + move[d][0]*i
        dy = y + move[d][1]*i

        if 0 <= dx < M and  0 <= dy < N and g[dx][dy] == 0 and check:
            if visited[d][dx][dy] > visited[d][x][y] + 1:
                visited[d][dx][dy] = visited[d][x][y]+1
                q.append([dx, dy, d])
        else:
            check = False
    if d == 1 or d == 2:
        index = 2 if d == 1 else 1


        if x+1 < M and visited[3][x][y] > visited[d][x][y] + 1 and g[x+1][y] == 0:
            visited[3][x][y] = visited[d][x][y] + 1
            q.append([x, y, 3])
        if x-1 >= 0 and visited[4][x][y] > visited[d][x][y] + 1 and g[x-1][y] == 0:
            visited[4][x][y] = visited[d][x][y] + 1
            q.append([x, y, 4])
        if 0 < y + move[index][1] < N and visited[index][x][y] > visited[d][x][y] + 1 and g[x][y+move[index][1]] == 0:
            visited[index][x][y] = visited[d][x][y] + 2
            q.append([x, y, index])

    if d == 3 or d == 4:
        index = 4 if d == 3 else 3

        if y + 1 < N and visited[1][x][y] > visited[d][x][y] + 1 and g[x][y + 1] == 0:
            visited[1][x][y] = visited[d][x][y] + 1
            q.append([x, y, 1])
        if y - 1 >= 0 and visited[2][x][y] > visited[d][x][y] + 1 and g[x][y - 1] == 0:
            visited[2][x][y] = visited[d][x][y] + 1
            q.append([x, y, 2])
        if 0 < x + move[index][0] < N and visited[index][x][y] > visited[d][x][y] + 1 and g[x][x + move[index][0]] == 0:
            visited[index][x][y] = visited[d][x][y] + 2
            q.append([x, y, index])
# for i in visited:
#     for j in i:
#         print(j)
#     print()
print(visited[ed][ex-1][ey-1])