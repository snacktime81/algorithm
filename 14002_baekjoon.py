n = int(input())
nums = list(map(int, input().split()))

length = [0] * n
length[0] = 1

for i in range(1, n):
    m = 1
    for j in range(i):
        if(nums[j] < nums[i]):
            m = max(m, length[j] + 1)
        length[i] = m

l = max(length)

arr = [1001]

for i in range(n-1, -1, -1):
    if(length[i] == l and arr[-1] > nums[i]):
        arr.append(nums[i])
        l -= 1
arr.sort()
print(max(length))
for i in range(max(length)):
    print(arr[i], end=' ')