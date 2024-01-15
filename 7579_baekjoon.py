N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
sum_costs = sum(costs)
dp = [[0 for _ in range(sum_costs+1)] for _ in range(N+1)]
r = sum_costs
for i in range(1, N+1):
    memory = memories[i]
    cost = costs[i]
    for j in range(sum_costs + 1):
        if(j > r):
            break
        if(j < cost):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)
        if(dp[i][j] >= M):
            r = min(r, j)
print(r)

