#https://www.acmicpc.net/problem/11055

n = int(input())
line = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    num = line[i]
    dp[i] = num
    d = dp[i]
    
    for j in range(i):
        preNum = line[j]
        preD = dp[j]
        
        if(preNum < num and dp[i] < (preD + num)):
            dp[i] = preD + num
            
print(max(dp))