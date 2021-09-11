#3036
import sys

n = int(sys.stdin.readline())
rings = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
  f_ring = rings[0]
  ring = rings[i]
  if f_ring == ring:
    print("1/1")
  elif f_ring > ring:
    while ring != 0:
      k = f_ring % ring
      f_ring = ring
      ring = k
    print(f"{rings[0]//f_ring}/{rings[i]//f_ring}")
  else:
    while f_ring != 0:
      k = ring % f_ring
      ring = f_ring
      f_ring = k
    print(f"{rings[0]//ring}/{rings[i]//ring}")

