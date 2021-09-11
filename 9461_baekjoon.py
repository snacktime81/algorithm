#9461
import sys

n = int(sys.stdin.readline())


def P(n):
  if n < 11:
    return p[n]
  else:
    p.append(P(n-1) + p[n-5])
    return p[n]

for i in range(n):
  p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
  num = int(sys.stdin.readline())
  print(P(num))