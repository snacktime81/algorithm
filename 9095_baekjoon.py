#9095
# f(n) = f(n-1) + f(n-2) + f(n-3)
import sys

T = int(sys.stdin.readline())

for _ in range(T):
  n = int(sys.stdin.readline())
  cnt = [0 for _ in range(n)]
  for i in range(n):
    if i <= 2:
      cnt[i] = 2 ** i
    else: 
      cnt[i] = cnt[i-1] + cnt[i-2] + cnt[i-3]
  print(cnt[n-1])