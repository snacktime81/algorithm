# https://www.acmicpc.net/problem/1149

n = int(input())

graph = []

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    
d = {0:[1,2], 1:[0,2], 2:[0,1]}
    
for i in range(1, n):
    for j in range(3):
        a, b = d[j]
        graph[i][j] += min(graph[i-1][a], graph[i-1][b])

print(min(graph[-1]))