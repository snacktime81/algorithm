#2805
import sys

n, m =map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
k = max(trees)

bottom = 0
top = k
while bottom <= top:
  mid = (bottom+top) // 2
  wood = 0
  for i in trees:
    left = i - mid
    if left > 0:
      wood += left
    else:
      continue
  if wood < m:
    bottom = mid + 1
  elif wood > m:
    bottom = mid - 1
  else:
    print(top)
    break

  
