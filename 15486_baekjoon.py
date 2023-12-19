import sys

input = sys.stdin.readline

coun = [[0,0]]
n = int(input())

works = []

dp = [0] * (n+1)

for i in range(1, n+1):
    a, b = map(int, input().split())    
    value = dp[i-1]+b
    dp[i] = max(dp[i-1], dp[i])
    if(i+a-1 <= n):
        dp[i+a-1] = max(value, dp[i+a-1])
    
print(max(dp))