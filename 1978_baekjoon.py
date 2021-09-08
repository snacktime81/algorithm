#1978
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
max_num = max(nums)

odd = [2, 3]
for i in range(4, max_num+1):
  for j in odd:
    if i % j == 0:
      k = False
      break
    else:
      k = True
  if k:
    odd.append(i)

cnt = 0
for i in nums:
  if i in odd:
    cnt += 1
  else:
    continue
print(odd)
print(cnt)
