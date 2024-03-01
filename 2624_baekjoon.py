import sys

input = sys.stdin.readline

T = int(input())
k = int(input())
coins = []
for _ in range(k):
    a, b = map(int, input().split())
    coins.append([a, b])

dp = [[0] * (T+1) for _ in range(k+1)]

for i in range(1, k+1):
    coin, cnt = coins[i-1]

    cost = coin
    for _ in range(cnt):
        if cost > T:
            break
        for j in range(1, T+1):
            if j-cost > 0 and dp[i-1][j-cost]:
                dp[i][j] += dp[i-1][j-cost]
        dp[i][cost] += 1
        cost += coin
    for j in range(1, T+1):  # 중요! 리스트 갱신은 1번만 진해해야 한다.
        dp[i][j] += dp[i-1][j]

#for i in dp:
#    print(i)
print(dp[-1][T])