# https://www.acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

n = int(input())

costs = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(n):
    dp[i+1] = costs[i]
    
for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
        
print(max(dp))