import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


R, C = map(int, input().split())
distance = [[0 for _ in range(C)] for _ in range(R)]

graph = []


man = []  # 사람 시작 좌표
fire = []  # 화점 시작 좌표

for i in range(R):
    line = list(input().strip())
    graph.append(line)

    for j in range(C):
        if(line[j] == 'J'):
            man.append(i)
            man.append(j)
        elif(line[j] == 'F'):
            fire.append([i,j])

q = deque()
for x, y in fire:
    q.append([x, y, 0])
q.append([man[0], man[1], 1])

check = 0

while q:
    x, y, state = q.popleft()

    if(state == 0):
        for i in move:
            dx = x + i[0]
            dy = y + i[1]

            if(dx < 0 or dx >= R or dy < 0 or dy >= C or graph[dx][dy] == '#' or graph[dx][dy] == 'F'):  # 불이 번질 수 없는 상황
                continue
            graph[dx][dy] = 'F'
            q.append([dx, dy, 0])
    else:
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            if(dx < 0 or dx >= R or dy < 0 or dy >= C ): # 탈출 조건
                check = distance[x][y] + 1
                break
            if(graph[dx][dy] == '#' or graph[dx][dy] == 'F'): # 갈 수 없는 좌표
                continue
            if(distance[dx][dy] != 0): # 이미 방문한 좌표
                continue
            distance[dx][dy] = distance[x][y] + 1
            q.append([dx, dy, 1])

    if(check):
        break

if(check):
    print(check)
else:
    print('IMPOSSIBLE')