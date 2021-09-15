#13241
import sys

n, m = map(int, sys.stdin.readline().split())
const_n = n
const_m = m


if n > m:
  while m != 0:
    k = n % m
    n = m
    m = k
    key = n
else:
  while n != 0:
    k = m % n
    m = n
    n = k
    key = m

if key == 1:
  print(const_n * const_m)
else:
  if const_m > const_n:
    print(const_m)
  else:
    print(const_n)