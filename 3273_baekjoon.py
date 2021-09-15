#3273
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
cnt = 0

for i in nums:
  if k < i:
    continue
  else:
    key = k - i
    if key in nums:
      cnt += 1
    else:
      continue
  
print(cnt//2)