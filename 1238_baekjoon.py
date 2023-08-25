import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

INF = int(1e9)

cost = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = c

    
for i in range(n+1):
    cost[i][i] = 0

for i in range(n+1):
    for j in range(n+1):
        for p in range(n+1):
            cost[i][j] = min(cost[i][j], cost[i][p]+cost[p][j])

            
result = []

for i in range(1, n+1):
    result.append(cost[i][x] + cost[x][i])

print(max(result))