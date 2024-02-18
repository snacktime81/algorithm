INF = int(1e9)

N, M = map(int, input().split())  # 마감일, 필요 가산점
vol = [0] + list(map(int, input().split()))
benefit, rest = map(int, input().split())  # 헌혈 점수, 휴식 일

result = INF

dp = [[0] * (N+rest) for _ in range(N//rest+rest)]
c = False

for i in range(1, N+rest):
    if(i <= N):
        dp[0][i] = dp[0][i-1] + vol[i]
        if(dp[0][i] >= M):
            result = 0
            c = True
if(c):
    print(result)
else:
    for i in range(1, N//rest+rest):
        for j in range(1, N+rest):
            if(j > N):
                dp[i][j] = dp[i-1][j-rest] + benefit
            elif(j-rest < 0):
                dp[i][j] = dp[i][j-1] + vol[j]
            else:
                dp[i][j] = max(dp[i-1][j-rest] + benefit, dp[i][j-1] + vol[j])
            if(dp[i][j] >= M):
                result = i
                c = True
                break
        if(c):
            break

    if(result == INF):
        print(-1)
    else:
        print(result)
