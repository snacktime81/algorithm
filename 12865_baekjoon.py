#https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline

n, k = map(int, input().split()) # 물품 수, 들 수 있는 무게

dp = [[0] * (k+1) for _ in range(n+1)]
things = [[0,0]]

for _ in range(n):
    
    thing = list(map(int, input().split())) # 무게와 가치가 들어간다
    things.append(thing)
    
for i in range(0, k+1):
    dp[0][i] = 0
for j in range(0, n+1):
    dp[j][0] = 0
        

for i in range(1, n+1):
    w, v = things[i]
    for j in range(1, k+1):
        if(j < w):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
mv = 0         
for i in dp:
    mv = max(max(i), mv)
    
print(mv)