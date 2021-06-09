#2606
import sys
computer = int(sys.stdin.readline())
n = int(sys.stdin.readline())
network = []

for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  if a == 1:
    if b not in network:
      network.append(b)
    else:
      continue
  else:
    if a in network and b not in network:
      network.append(b)
    else:
      continue
print(len(network))
