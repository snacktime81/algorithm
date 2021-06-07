#1931
import sys
N = int(sys.stdin.readline())
meeting = {}
li = []
clock = []
l = []

# 시간초과, 정렬파트 간소화 필요함
for i in range(N):
  time = list(sys.stdin.readline().split())
  using_time = int(time[1]) - int(time[0])
  meeting[i] = using_time
  li.append(time)

meeting_sort = sorted(meeting.items(), key = lambda x: x[1])
for i in range(len(meeting_sort)):
  l.append(meeting_sort[i][0])

table = []

for i in l:
  table.append(li[i])

can = True # 회의시간이 겹치지 않으면 True 겹치면 False
count = 0
for i in table:
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
    for _ in range(int(i[1])-int(i[0])-1):
      a += 1
      clock.append(a)
    count += 1
  else:
    can = True
    continue

print(count)
