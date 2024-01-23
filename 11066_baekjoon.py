import sys

input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    dp=[[0] * (n+1) for _ in range(n+1)]
    s = [0] * (n+1)
    
    for i in range(n):
        s[i+1] = s[i] + nums[i]
        
    for i in range(n, 0, -1):
        for j in range(i+1, n+1):
            tmp = INF
            diff = s[j] - s[i-1]
            for k in range(i, j):
                tmp = min(tmp, dp[i][k] + dp[k+1][j] + diff)
            dp[i][j] = tmp
    print(dp[1][n])
            