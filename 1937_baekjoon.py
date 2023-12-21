import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, costs):

    if(costs[x][y] != -1):
        return costs[x][y]
    costs[x][y] = 1
    value = graph[x][y]

    for i in move:
        dx = x + i[0]
        dy = y + i[1]

        if(dx <0 or dy < 0 or dx >= n or dy >= n or value >= graph[dx][dy]):
            continue

        count = 1
        count += dfs(dx, dy, costs)
        costs[x][y] = max(costs[x][y], count)
        
    return costs[x][y]
            
            

n = int(input())

graph = []
move = [(1,0), (0,1), (-1, 0), (0, -1)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

costs = [[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(costs[i][j] == -1):
            dfs(i, j ,costs)
r = 0

for cost in costs:
    r = max(r, max(cost))
print(r)