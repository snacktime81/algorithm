N = int(input())
NUMS = [-1] + list(map(int, input().split()))

dp = [[0, 0, 0] for _ in range(N+1)]  # i번째 수 삭제, i번째수 비삭제, i번째 까지의 누적합(양수)
r = -1001
for i in range(1, N+1):
    num = NUMS[i]
    dp[i][2] = (dp[i-1][2] if dp[i-1][2] > 0 else 0) + num 
    dp[i][1] = max(dp[i-1]) + num
    dp[i][0] = dp[i-1][2] if dp[i-1][2] > 0 else num
    r = max(r, dp[i][2], dp[i][1], dp[i][0])
    
print(r)
