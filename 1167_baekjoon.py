# https://moonsbeen.tistory.com/101
# 증명도움

import sys
from collections import deque

input = sys.stdin.readline


def bfs(node, g):
    visited = [-1] * (N+1)
    visited[node] = 0
    q = deque([(node)])

    while q:
        node = q.popleft()

        for i in g[node]:
            if visited[i[0]] == -1:
                visited[i[0]] = visited[node] + i[1]
                q.append(i[0])
    return visited


N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N):
    line = list(map(int, input().split()))
    num = line[0]
    for i in range(1, len(line)-1, 2):
        node = line[i]
        cost = line[i+1]
        g[num].append([node, cost])


tmp = bfs(1, g)
index = 0
m = 0
for i in range(1, N+1):
    if tmp[i] > m:
        m = tmp[i]
        index = i
print(max(bfs(index, g)))