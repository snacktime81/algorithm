# https://www.acmicpc.net/problem/9084

import sys
from copy import deepcopy
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    line = list(map(int, input().split()))
    m = int(input())
    coins = [0] + line
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
        
    for i in range(1, n+1):
        coin = coins[i]
        dp[i] = deepcopy(dp[i-1])
        for j in range(m+1):
            if(j-coin >= 0):
                dp[i][j] += dp[i][j-coin]
            
    
    print(dp[-1][-1])