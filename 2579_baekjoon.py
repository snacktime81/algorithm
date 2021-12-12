#2579
import sys

stairs = int(sys.stdin.readline())
score = [0 for _ in  range(stairs+1)]
sum_score = 0

for i in range(stairs - 1, -1, -1):
  score[i] = int(sys.stdin.readline())
score[stairs] = 0

B = True

tmp = 1
sum_score += score[0]
cnt = 1

while(cnt < stairs):
  if tmp == 2:
    cnt += 2
    sum_score += score[cnt]
    tmp = 1
  else:
    if score[cnt] > score[cnt+1]:
      sum_score += score[cnt]
      tmp += 1
      cnt += 1
    else:
      sum_score += score[cnt+1]
      tmp = 1
      cnt += 2

print(sum_score)