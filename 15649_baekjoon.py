# from itertools import permutations

# N, M = map(int, input().split())

# nums = [i for i in range(1, N+1)]

# data = list(permutations(nums, M))
# for i in data:
#     for j in i:
#         print(j, end=' ')
#     print()

# 2
# N, M = map(int, input().split())
# nums = [i for i in range(1, N+1)]
#
# dp = [[] for _ in range(M+1)]
#
# for i in range(1,N+1):
#     dp[1].append([i])
#
# for i in range(2, M+1):
#     tmp = []
#
#     for num in nums:
#         for j in dp[i-1]:
#             if(num not in j):
#                 dp[i].append([num] + j)
# for i in dp[-1]:
#     for j in i:
#         print(j, end=' ')
#     print()


# 3
N, M = map(int, input().split())

arr = []

def dfs(num, visited, result):
    visited[num] = True
    result += str(num) + ' '
    #print(num)
    if len(result) == M * 2:
        arr.append(result.rstrip())
        return 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i, visited, result)
            visited[i] = False

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, visited, '')
    visited[i] = False
for i in arr:
    print(i)