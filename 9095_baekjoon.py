#9095

import sys

T = int(sys.stdin.readline())
cnt = []

for _ in range(T):
  n = int(sys.stdin.readline())
  k = 1
  for i in range(n):
    if k == 1:
      cnt.append(1)
    else:
      