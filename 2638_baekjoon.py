import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def fill(graph):
    N = len(graph)
    M = len(graph[0])
    
    visited = [[False] * (M) for _ in range(N)]
    
    que = deque([(0, 0)])
    graph[0][0] = 2
    visited[0][0] = True
    
    while que:
        x, y = que.popleft()
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            if(dx < 0 or dx >= N or dy < 0 or dy >= M):
                continue
            if not visited[dx][dy] and graph[dx][dy] != 1:
                que.append([dx, dy])
                graph[dx][dy] = 2
                visited[dx][dy] = True


def remove(graph):
    N = len(graph)
    M = len(graph[0])
    
    tmp_graph = deepcopy(graph)
    
    for x in range(N):
        for y in range(M):
            if(graph[x][y] == 1):
                cnt = 0
                for i in move:
                    dx = x + i[0]
                    dy = y + i[1]
                    if(graph[dx][dy] == 2):
                        cnt += 1
                if(cnt >= 2):
                    tmp_graph[x][y] = 0
    return tmp_graph


def check(graph):
    for i in graph:
        for j in i:
            if(j == 1):
                return False
    return True


N, M = map(int, input().split())

graph = []

for _ in range(N):
    line = list(map(int, input().split()))
    
    graph.append(line)

result = 0
while not check(graph):
    result += 1
    fill(graph)
    graph = deepcopy(remove(graph))

print(result)
