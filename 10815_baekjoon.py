import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
s.sort()

result = []

for i in nums:
  top = n
  bottom = 0
  while bottom <= top:
    mid = (top+bottom)//2
    if top == bottom:
      if i != s[mid]:
        result.append(0)
      else:
        result.append(1)
      break
    if i < s[mid]:
      top = mid - 1
    elif i > s[mid]:
      bottom = mid + 1
    elif i == s[mid]:
      result.append(1)
      break


for i in result:
  print(i, end=" ")