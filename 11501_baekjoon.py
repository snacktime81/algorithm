#11501
import sys
n = int(sys.stdin.readline())
profits= []
for i in range(n):
  m = int(sys.stdin.readline())
  stocks = list(map(int, sys.stdin.readline().split()))
  max_price = max(stocks)
  profit = 0
  cnt = 0 
  for i, price in enumerate(stocks):
    if i == 0 and price < max_price:
      profit -= price
      cnt += 1
    else:
      stocks_right = stocks[i:]
      max_price = max(stocks_right)
      if price < max_price:
        profit -= price
        cnt += 1
      elif price == max_price:
        profit += max_price * cnt
        cnt = 0
  profits.append(profit)

for i in profits:
  print(i)
    