N = int(input())
NUMS = list(map(int, input().split()))

dp = [1] * (N)

for i in range(N):
    num = NUMS[i]

    for j in range(i):
        tmp = NUMS[j]
        if(tmp > num):
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))