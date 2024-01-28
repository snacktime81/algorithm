import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):
    line = input().rstrip()
    arr = []
    for i in line:
        arr.append(int(i))
    graph.append(arr)
    
for x in range(1, N):
    for y in range(1, M):
        if(graph[x][y] == 1):
            a = graph[x-1][y]
            b = graph[x][y-1]
            c = graph[x-1][y-1]

            graph[x][y] = min(a, b, c) + 1

r = 0
for i in graph:
    r = max(r, max(i))
print(r**2)