import sys

rope = []
n = int(sys.stdin.readline())
for i in range(n):
  rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

w = []
for i in range(n):
  k = i+1
  w.append(k*rope[i])

print(max(w))
  