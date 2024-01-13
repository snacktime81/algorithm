import sys
input = sys.stdin.readline
T, W = map(int, input().split())

dp = [[0 for _ in range(T+1)] for _ in range(W+1)]

plums = [1]

for i in range(T):
    plum = int(input())
    plums.append(plum)
tmp = 0
for i in range(1, T+1):
    if(plums[i] == 1):
        tmp += 1
    dp[0][i] = tmp
    
for move in range(1, W+1):
    for time in range(1, T+1):
        now = 1 if move%2 == 0 else 2 #  현재 자두(사람)가 있는 우치
        plum = plums[time] #  현재 자두가 떨어지는 위치
        if(now == plum):
            try:
                if(plum != plums[time-1]):
                    dp[move][time] = max(dp[move][time-1], dp[move-1][time-1]) + 1
                else:
                    dp[move][time] = dp[move][time-1] + 1
            except:
                dp[move][time] = 1
        else:
            dp[move][time] = dp[move][time-1]
r = 0

for i in dp:
    r = max(i[-1], r)
print(r)