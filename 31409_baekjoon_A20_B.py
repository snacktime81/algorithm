N = int(input())
nums = [0] + list(map(int, input().split()))

cnt = 0

for i in range(1, N+1):
    if(i == nums[i]):
        tmp = i+1 if i+1 <= N else i-1
        nums[i] = tmp
        cnt += 1
print(cnt)
for i in range(1, N+1):
    print(nums[i], end=' ')