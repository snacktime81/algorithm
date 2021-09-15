#3273
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
k = int(sys.stdin.readline())
cnt = 0

for i in nums:
  if k < i:
    continue
  else:
    key = k - i
    bottom = 0
    top = n-1
    while bottom <= top:
      mid = (top+bottom) // 2
      if nums[mid] > key:
        top = mid - 1
      elif nums[mid] < key:
        bottom = mid + 1
      elif nums[mid] == key:
        cnt += 1
        break
      else:
        continue
  
print(cnt//2)