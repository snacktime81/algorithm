#2512
import sys
n = int(sys.stdin.readline())
moneys = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
sum_money = sum(moneys)
tmp = 0
cnt = 0

if sum_money <= m:
  print(max(moneys))
else:
  average_money = m // n
  for i in moneys:
    if average_money >= i:
      tmp += (average_money - i)
    else:
      cnt += 1
  k = tmp // cnt
  print(average_money + k)
