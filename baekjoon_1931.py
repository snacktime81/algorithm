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


# 수정 바람
for i in table:
  k = i[1]

  if k not in clock:
    continue
  else:
    for _ in range(i[1]-i[0] - 1):
      k += 1
      clock.remove(k)
  


