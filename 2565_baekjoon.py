N = int(input())

line = []

for _ in range(N):
    s, e = map(int, input().split())
    line.append([s, e])
    
line.sort()


dp = [1] * (N+1)

for i in range(N):
    for j in range(i):
        if(line[i][1] > line[j][1]):
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))