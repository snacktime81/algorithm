# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations
INF = int(1e9)

graph = []

n, m = map(int, input().split())
chickens = []
houses = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 2):
            chickens.append([i, j])
            graph[i][j] = 0
        elif(graph[i][j] == 1):
            houses.append([i, j])

dataC = list(combinations(chickens, m))

result = INF

for data in dataC:
    r = 0
    
    for house in houses:
        tmp = INF
        for chicken in data:
            cost = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            tmp = min(cost, tmp)
            
        r += tmp
    result = min(result, r)

print(result)