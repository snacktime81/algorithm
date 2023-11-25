# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input())

tables = []

for _ in range(n):
    tables.append(int(input()))

dp = []

if(n == 1):
    print(tables[0])
elif(n == 2):
    print(sum(tables))
else:

    dp.append(tables[0])
    dp.append(tables[1]+tables[0])
    dp.append(max(dp[1], dp[0] + tables[2], tables[1]+tables[2]))

    for i in range(3, n):
        tmp = max(dp[i-2] + tables[i], dp[i-1], dp[i-3] + tables[i-1] + tables[i]) # 점화 식 f(n) = max(f(n-2) + Wn, f(n-1), f(n-3) + Wn-1 + Wn)
        dp.append(tmp)
    
    print(max(dp))
