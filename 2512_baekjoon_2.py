import sys
n = int(sys.stdin.readline())
moneys = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
sum_money = sum(moneys)

bottom = 0
top = max(moneys)
if sum_money <= m:
  print(top)
else:
  while(bottom <= top):
    mid = (bottom + top) // 2
    tmp = 0
    for i in moneys:
      if i >= mid:
        tmp += mid
      else:
        tmp += i
    if m < tmp:
      top = mid - 1
    else:
      bottom = mid + 1
  print(top)