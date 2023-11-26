import sys
input = sys.stdin.readline

n = int(input())

T = []
P = []

for _ in range(n):
    Ti, Pi = map(int, input().split())
    T.append(Ti)
    P.append(Pi)
    
dp = [0]*(n+1) # 제일 마지막 날에 T가 1이면 out out range가 발생해서 n+1으로 생성

for i in range(n-1, -1, -1):
    Ti = T[i]
    Pi = P[i]
    
    if(Ti + i > n):
        dp[i] = max(dp)
        continue
        
    
    maxC = max(dp[i:i+Ti])

    dp[i] = max(maxC, dp[i+Ti]+P[i])
    
print(max(dp))