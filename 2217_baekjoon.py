import sys
import math

rope = []
n = int(sys.stdin.readline())
for i in range(n):
  rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

w = []
for i in range(math.ceil(n/2)):
  k = i+1
  cnt = rope.count(rope[i])
  w.append(k*rope[i])

print(max(w))
  