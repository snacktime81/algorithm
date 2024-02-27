N, S = map(int ,input().split())
nums = list(map(int ,input().split()))

sums = [0]

for i in range(N):
    sums.append(sums[i] + nums[i])

if sums[-1] < S:
    print(0)
else:
    left = 0
    right = 1

    cnt = N

    while left < right and right <= N:
        v = sums[right] - sums[left]
        if v < S:
            right += 1
        elif v >= S:
            cnt = min(right - left, cnt)
            left += 1
    print(cnt)