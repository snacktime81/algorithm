#2805
import sys

n, m =map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
k = max(trees)

while True:
  wood = 0
  for tree in trees:
    left_wood = tree - k
    if left_wood > 0:
      wood += left_wood
    else:
      continue
  if wood >= m:
    break
  else:
    k -= 1
  
print(k)
