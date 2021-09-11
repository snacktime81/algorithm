#9462
import sys
t = int(sys.stdin.readline())

for i in range(t):
  p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
  n = int(sys.stdin.readline())
  if n < 11:
    print(p[n])
  else:
    for i in range(11, n+1):
      p.append(p[i - 1]+p[i - 5])

    print(p[n])