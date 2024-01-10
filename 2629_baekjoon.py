n = int(input())
weights = list(map(int, input().split()))
m = int(input())
balls = list(map(int ,input().split()))

DEPTH = 55001
dp = [[0] * (DEPTH) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    now = weights[i-1]
    for j in range(1, DEPTH):
        dp[i][j] = dp[i-1][j]
        
        if(dp[i-1][j-now] == 1):
            dp[i][j] = 1

for i in balls:
    if(dp[-1][i] == 1):
        print('Y', end=' ')
    else:
        c = False
        for j in range(DEPTH):
            now = i + j
            if(dp[-1][j]==1 and dp[-1][now] == 1): # 추가 a,b,c 라면 x+a = b+c 이면 측정가능한 무게이다. 
                c = True
                break
        if(c):
            print('Y', end=' ')
        else:
            print('N', end=' ')

# for i in dp:
#     print(i)