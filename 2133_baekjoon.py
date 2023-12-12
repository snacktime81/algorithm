# https://www.acmicpc.net/problem/2133

n = int(input())

dp = [0] *(30+1)
dp[0] = 1
dp[2] = 3
dp[3] = 0

if(n<4):
    print(dp[n])
else:
    for i in range(4, n+1, 2):
        a = dp[i-2]*3
        b = 0
        for j in range(4, i, 2):
            b += dp[i-j] * 2
        dp[i] = a + b + 2
    print(dp[n])
    
    