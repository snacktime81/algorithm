import sys

n = int(sys.stdin.readline())
level = []
for i in range(n):
  level.insert(0, int(sys.stdin.readline()))

cnt = 0
for i in range(1, len(level)):
  if level[i] < level[i-1]:
    continue
  else:
    while True:
      if level[i] < level[i-1]:
        break
      else:
        level[i] -= 1
        cnt += 1
print(cnt)
