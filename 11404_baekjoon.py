import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

cost = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    
    cost[a-1][b-1] = min(cost[a-1][b-1], c)
for i in range(n):
    for a in range(n):
        for b in range(n):
            if(a == b):
                cost[a][b] = 0
            cost[a][b] = min(cost[a][i] + cost[i][b], cost[a][b])
    
for i in cost:
    for j in i :
        if(j == INF):
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()