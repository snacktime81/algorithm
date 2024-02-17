N = int(input())
nums = list(map(int, input().split()))

key = nums[0]
cnt = 0
dp = [-1] * (N+1)
que = [[1000001, 1000001]] # value, index

for i in range(N):
    num = nums[i]
    if(num > que[-1][0]):
        while num > que[-1][0]:
            dp[que[-1][1]] = num
            que.pop()
        que.append([num, i])
    else:
        que.append([num, i])
for i in range(N):
    print(dp[i], end=' ')