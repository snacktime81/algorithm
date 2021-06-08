#1931
import sys
N = int(sys.stdin.readline())
meeting = {}
li = []
clock = []

# 시간초과, 정렬파트 간소화 필요함
for i in range(N):
  time = list(sys.stdin.readline().split())
  using_time = int(time[1]) - int(time[0])
  meeting[int(time[0])] = using_time  # 회의 시작 시간이 같으면 딕셔너리 특성상 앞에 회의시간이 사라진다.

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
    a = i
    for _ in range(j-1):
      a += 1
      clock.append(a)
    count += 1
  else:
    can = True
    continue

print(count)
