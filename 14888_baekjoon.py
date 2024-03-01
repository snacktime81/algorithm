from collections import deque
from copy import copy

N = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))

n = nums[0]
q = deque([(1, cal, n)])

max_v = -int(1e10)
min_v = int(1e10)

while q:
    index, cal, sum = q.popleft()
    #print(cal, sum)
    if index == N:
        max_v = max(max_v, sum)
        min_v = min(min_v, sum)
        continue
    num = nums[index]
    if cal[0] > 0:
        tmp = copy(cal)
        tmp[0] -= 1
        q.append([index+1, tmp, sum+num])
    if cal[1] > 0:
        tmp = copy(cal)
        tmp[1] -= 1
        q.append([index + 1, tmp, sum - num])
    if cal[2] > 0:
        tmp = copy(cal)
        tmp[2] -= 1
        q.append([index + 1, tmp, sum * num])
    if cal[3] > 0:
        tmp = copy(cal)
        tmp[3] -= 1
        if sum < 0:
            sum = abs(sum) // num * -1
        else:
            sum = sum//num
        q.append([index + 1, tmp, sum])


print(max_v)
print(min_v)