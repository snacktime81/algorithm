# https://www.acmicpc.net/problem/1106

import sys
input = sys.stdin.readline
INF = int(1e9)
c, n = map(int, input().split())

customers = [[0,0]]

for _ in range(n):
    customers.append(list(map(int, input().split())))

dp = [INF] * (1111)
dp[0] = 0
for i in range(1, n+1):
    cost, eff = customers[i]
    for j in range(1, 1111):
        if(j-eff >= 0):
            dp[j] = min(dp[j-eff]+cost, dp[j])
print(min(dp[c:]))
