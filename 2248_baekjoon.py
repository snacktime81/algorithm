N, L, I = map(int, input().split())

dp = [[0] * (N+1) for _ in range(L+1)]

for i in range(N+1):
    dp[0][i] = 1
for i in range(L+1):
    dp[i][0] = 1

for i in range(1, L+1):
    for j in range(1, N+1):
        if(i == j):
            dp[i][j] = 2 ** i
            continue
        dp[i][j] = max(dp[i][j-1] + dp[i-1][j-1], dp[i-1][j])

result = ''


def find(a, b, c, result):
    print(a, b, c)
    if(a == 0):
        return result
    if(dp[b][a-1] < c):
        result += '1'
        return find(a-1, b-1, c-dp[b][a-1], result)
    elif(dp[b][a-1] >= c):
        result += '0'
        return find(a-1, b, c, result)


result = find(N, L, I, result)

print(result)