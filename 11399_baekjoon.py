#11399
import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
li2 = []
li2.append(li[0])
for i in range(1, n):
  k = li[i] + li2[i-1]
  li2.append(k)

print(sum(li2))
