#14490
import sys

n = sys.stdin.readline().strip()
li_n = list(n)
k = li_n.index(":")
num1 = int(n[:k])
num2 = int(n[k+1:])
a = num1
b = num2

if num1 > num2:
  while num2 > 0:
    num1, num2 = num2, num1 % num2
    o = num1
else:
  while num1 > 0:
    num2, num1 = num1, num2 % num1
    o = num2
num1 = a // o
num2 = b // o
print(str(num1)+":"+str(num2))