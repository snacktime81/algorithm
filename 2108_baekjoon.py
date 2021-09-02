#2108
import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
  li.append(int(sys.stdin.readline()))

li.sort()
lst = tuple(li)
l = {}
l2 = []
for i in lst:
  k = li.count(i)
  l2.append(k)
  l[i] = k
l3 = sorted(l.items(), key=lambda x: x[1])


first = round(sum(li)/len(li))
second = li[round(len(li)/2)]


a = max(l2)
l2.remove(a)
if len(li) > 2:
  b = max(l2)

  if l3[a][1] == l3[b][1]:
    third = l[b]
  else:
    third = l[a]
else:
  third = l[a]

four = max(li) - min(li)

print(first)
print(second)
print(third)
print(four)