import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

NUMS = []

for _ in range(N):
    NUMS.append(int(input()))

dp = [INF] * (N+1)

dp[-1] = 0
dp[N-1] = 0

for i in range(N-2, -1, -1):
    num = NUMS[i]
    dp[i] = (M-num) ** 2 + dp[i+1]
    num += 1
    
    for j in range(i+1, N):
        num += NUMS[j]
        if(num > M):
            break
        if(j == N-1):
            dp[i] = 0
            break
        dp[i] = min(dp[i], (M-num)**2 + dp[j+1])
        num += 1
print(dp[0])