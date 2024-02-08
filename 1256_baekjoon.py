# 비슷한 문제 https://www.acmicpc.net/problem/2248

N, M, K = map(int, input().split())


dp = [[0] * (N+M+1) for _ in range(M+1)] # dp[글자수][z의 개수]

for i in range(N+M+1):
    dp[0][i] = 1
    
for i in range(1, N+M+1):
    for j in range(1, M+1):
        if(i - j > N): # i-j는 a의 개수이며 a의 개수가 N을 넘을때는 제외
            continue
        dp[j][i] = dp[j-1][i-1] + dp[j][i-1]

a = N+M
b = M
c = K
result = ''

max_k = dp[-1][-1]

    

if(K > max_k):
    print(-1)
else:
    for _ in range(a):

        if(dp[b][a-1] < c):
            result += 'z'
            c -= dp[b][a-1]
            a -= 1
            b -= 1
        else:
            result += 'a'
            a -= 1
    print(result)
        
