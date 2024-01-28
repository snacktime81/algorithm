from copy import copy

N = int(input())
NUMS = [0] + list(map(int, input().split()))

dp =[[0] * (N + 1) for _ in range(N + 1)]

dp1 = [0] * (N+1)
dp2 = [0] * (N+1)

for i in range(N-1, 0, -1):
    for j in range(i+1, N+1):
        if(NUMS[i] == NUMS[j]):
            dp1[j] = dp2[j-1]
        else:
            dp1[j] = min(dp1[j-1], dp2[j]) + 1
    dp2 = copy(dp1)
    r = dp1[N]
    dp1 = [0] * (N+1)
print(r)