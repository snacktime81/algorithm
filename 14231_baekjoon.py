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

print(const_n * const_m // key)