#https://www.acmicpc.net/problem/2225

n, m = map(int, input().split()) # 숫자, 개수

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

'''
f(n, m) = sum(f(0~n, m-1)) = f(n, m-1) + f(n-1, m) 


6을 4개로 만드는 법은 

6을 3개로 만드는 방법 + 0
5를 3개로 만드는 방법 + 1
4를 3개로 만드는 방법 + 2
...
0을 3개로 만드는 방법 + 6

'''

for i in range(n+1):
    dp[0][i] = 0
    dp[1][i] = 1
for i in range(m+1):
    dp[i][0] = 1
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000
            
print(dp[m][n])