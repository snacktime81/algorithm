#1931
import sys
N = int(sys.stdin.readline())
meeting = []
clock = []

# 시간초과
for i in range(N):
  h1, h2 = map(int, sys.stdin.readline().split())
  using_time = h2 - h1
  li = [h1, using_time]
  meeting.append(li)
meeting.sort(key=lambda x:x[1])
can = True # 회의시간이 겹치지 않으면 True 겹치면 False
count = 0
for i in meeting:
  k = i[0] + i[1]
  c = i[0]
  while c != k + 1:
    if c not in clock:
      c += 1
    else:
      can = False
      break
  
  if can:
    a = int(i[0])
    for _ in range(i[1]-1):
      a += 1
      clock.append(a)
    count += 1
  else:
    can = True
    continue

print(count)