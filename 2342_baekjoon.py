INF = int(1e9)

def move(lr, k):
    if k == 0:
        if lr == 0:
            return 0
        else:
            return 2
    elif k == lr:
        return 1
    elif abs(k - lr) == 1 or abs(k - lr) == 3:
        return 3
    else:
        return 4

commands = list(map(int, input().split()))
n = len(commands)

dp = [[[INF + 1 for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
dp[-1][0][0] = 0

for i in range(n):
    now = commands[i]
    for l in range(5):
        for r in range(5):
            if dp[i - 1][l][r] == -1:
                continue
            add = move(now, l)
            dp[i][now][r] = min(dp[i][now][r], dp[i - 1][l][r] + add)

            add = move(now, r)
            dp[i][l][now] = min(dp[i][l][now], dp[i - 1][l][r] + add)

m = INF + 1
for l in range(5):
    for r in range(5):
        m = min(m, dp[n - 2][l][r])
print(m)
