N = int(input())
TRAINS = [0] + list(map(int, input().split()))
M = int(input())

dp = [[0] * (N+1) for _ in range(4)]

people = [0] * (N+1)

for i in range(1, N+1):
    people[i] = people[i-1] + TRAINS[i]
    
for i in range(1, 4):
    for j in range(M*i, N+1):
        dp[i][j] = max(dp[i-1][j-M] + people[j]-people[j-M], dp[i][j-1])
print(max(dp[3]))