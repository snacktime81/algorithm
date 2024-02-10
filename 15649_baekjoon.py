# from itertools import permutations

# N, M = map(int, input().split())

# nums = [i for i in range(1, N+1)]

# data = list(permutations(nums, M))
# for i in data:
#     for j in i:
#         print(j, end=' ')
#     print()


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]

dp = [[] for _ in range(M+1)]

for i in range(1,N+1):
    dp[1].append([i])

for i in range(2, M+1):
    tmp = []
    
    for num in nums:
        for j in dp[i-1]:
            if(num not in j):
                dp[i].append([num] + j)
for i in dp[-1]:
    for j in i:
        print(j, end=' ')
    print()
    