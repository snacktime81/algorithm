import sys

input = sys.stdin.readline
    
T = int(input())

for _ in range(T):
    n = int(input())
    cards = [0] + list(map(int, input().split()))
    dp = [[[-1, -1] for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n, 0, -1):
        for j in range(i, n+1):
            if(i == j):
                dp[i][j][0] = cards[i]
                dp[i][j][1] = 0
            else:
                a = dp[i+1][j][1] + dp[i][i][0]
                b = dp[i][j-1][1] + dp[j][j][0]
                if( a > b):
                    dp[i][j][0] = a
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = b
                    dp[i][j][1] = dp[i][j-1][0]
    print(dp[1][n][0])
    