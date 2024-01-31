import sys

input = sys.stdin.readline

N = int(input())
NUMS = [201]

for _ in range(N):
    num = int(input())
    NUMS.append(num)

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = 1
    for j in range(1, i):
        if(NUMS[i] > NUMS[j]):
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))