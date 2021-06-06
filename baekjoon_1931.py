#1931
import sys
N = int(sys.stdin.readline())
meeting = {}
li = []
clock = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
l = []

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
    if c in clock:
      c += 1
    else:
      can = False
      break
  
  if can:
    a = int(i[0])
    for _ in range(int(i[1])-int(i[0])-1):
      a += 1
      clock.remove(a)
    count += 1
  else:
    can = True
    continue

print(count)
