#2805
import sys

n, m =map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
k = max(trees)

bottom = 1
top = k
result = 0
while bottom <= top:
  mid = (bottom+top) // 2
  wood = 0
  for i in trees:
    if i > mid:
      wood += i-mid
  if wood < m:
    top = mid - 1
  else:
    result = mid
    bottom = mid + 1
print(result)