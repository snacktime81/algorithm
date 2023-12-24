# https://www.acmicpc.net/problem/2482

import sys
imput = sys.stdin.readline
n = int(input())
k = int(input())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

if(k > n // 2):
    print(0)
else:
    for i in range(2, n+1):
        for j in range(2, k+1):
            if(i < n):
                dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003
            else:
                dp[i][j] = (dp[i-3][j-1] + dp[i-1][j]) % 1000000003
    print(dp[n][k])
