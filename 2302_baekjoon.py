#https://www.acmicpc.net/problem/2302

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

seats = [0]*n
for _ in range(m):
    seat = int(input())-1
    seats[seat] = 1
    
dp = [0] * (41)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1]+dp[i-2]
cnt = 0
result = 1
for i in seats:
    if(i == 0):
        cnt += 1
    if(i == 1):
        result *= dp[cnt]
        cnt = 0
if(cnt != 0):
    result *= dp[cnt]
print(result)