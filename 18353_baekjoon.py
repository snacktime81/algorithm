# https://www.acmicpc.net/problem/18353

n = int(input())
soliders = list(map(int, input().split()))

dp = []

for i in range(n):
    tmp = 1
    for j in range(i):
        if(soliders[i] < soliders[j]):
            tmp = max(tmp, dp[j] + 1)
    dp.append(tmp)
    
print(n-max(dp))