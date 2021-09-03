#11047
import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
  coins.append(int(sys.stdin.readline()))
m = n-1
count = 0
while k > 0:
  if k > coins[-1]*5:
    c = k // coins[-1]
    count += c
    k = k - coins[-1]*c
  else:
    for i in range(n):
      if coins[m - i] <= k:
        count += 1
        k = k - coins[m - i]
        break
      else:
        continue
print(count)