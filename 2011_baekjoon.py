line = list(input())
nums = [0]

for i in line:
    nums.append(int(i))
n = len(nums)
dp = [0] * (n)
dp[0] = 1

'''
2109

2 10 9


201

'''


check = False
for i in range(1,n):  
    if(nums[i] == 0):
        if(nums[i-1] > 2 or nums[i-1] == 0):
            check =True
            break
        if(nums[i-1] < 3):
            dp[i] = dp[i-2]
            continue
    if(nums[i-1] == 0):
        dp[i] = dp[i-1]
        continue
    if((nums[i-1] * 10) + nums[i] > 26):
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000

if(check):
    print(0)
else:
    print(dp)