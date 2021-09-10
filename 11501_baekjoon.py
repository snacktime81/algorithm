#11501
import sys
n = int(sys.stdin.readline())
profits= []
for _ in range(n):
  m = int(sys.stdin.readline())
  stocks = list(map(int, sys.stdin.readline().split()))
  max_price = stocks[-1]
  profit = 0
  for i in range(m-1, -1, -1):
    if stocks[i] < max_price:
      profit += max_price - stocks[i]
    else:
      max_price = stocks[i]
  profits.append(profit)
for i in profits:
  print(i)