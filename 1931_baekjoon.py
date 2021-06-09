#1931
import sys
N = int(sys.stdin.readline())
meeting = {}
li = []
clock = []

# 시간초과
for i in range(N):
  time = tuple(sys.stdin.readline().split()) # list는 dict의 key가 될 수 없다, 반면에 tuple은 dict의 key가 될 수 있다.
  using_time = int(time[1]) - int(time[0])
  meeting[time] = using_time 

meeting_sort = sorted(meeting.items(), key = lambda x: x[1])

can = True # 회의시간이 겹치지 않으면 True 겹치면 False
count = 0
for i, j in meeting_sort:
  k = int(i[1])
  c = int(i[0])
  while c != k + 1:
    if c not in clock:
      c += 1
    else:
      can = False
      break
  
  if can:
    a = int(i[0])
    for _ in range(j-1):
      a += 1
      clock.append(a)
    count += 1
  else:
    can = True
    continue

print(count)
