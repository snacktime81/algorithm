# https://www.acmicpc.net/problem/11053

n = int(input())
nums = list(map(int, input().split()))

dp = []

for i in range(n):
    tmp = 1
    for j in range(i):
        if(nums[i] > nums[j]):
            tmp = max(tmp,  dp[j]+1)
    dp.append(tmp)
    
print(max(dp))