# https://www.acmicpc.net/problem/2294
import sys
from copy import deepcopy
input = sys.stdin.readline
INF = int(1e9)
n, k = map(int, input().split())

dp = [INF] * (k+1)


dp[0] = 0

coins = [0]
for _ in range(n):
    coins.append(int(input()))
    
for i in range(1, n+1):
    coin = coins[i]
    for j in range(1, k+1):
        if(j-coin >= 0):
            dp[j] = min(dp[j-coin]+1, dp[j])

if(dp[-1] == INF):
    print(-1)
else:
    print(dp[-1])