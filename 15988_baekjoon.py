import sys

input = sys.stdin.readline

T = int(input())

nums = []

for _ in range(T):
    N = int(input())
    nums.append(N)

max_n = max(nums)


dp = [0] * (max_n + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4, max_n+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for n in nums:
    print(dp[n])