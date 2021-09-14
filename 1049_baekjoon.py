#1049
import sys
n, m = map(int, sys.stdin.readline().split())

set_cost_li = []
each_cost_li = []
cost = 0


for i in range(m):
  set_cost, each_cost = map(int, sys.stdin.readline().split())
  set_cost_li.append(set_cost)
  each_cost_li.append(each_cost)

min_cost = min(each_cost_li)
min_set_cost = min(set_cost_li)

if min_cost * 6 > min_set_cost:
  if n < 7:
    cost += min_set_cost
  else:
    while n > 6:
      n -= 6
      cost += min_set_cost 
    if n * min_cost < min_set_cost:
      cost += min_cost * n
    else:
      cost += min_set_cost
else:
  cost += n * min_cost

print(cost)