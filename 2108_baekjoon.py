#2108
import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
  li.append(int(sys.stdin.readline()))

li.sort()
li_third = []
for i in li:
  cnt = li.count(i)
  li_third.append([cnt, i])

li_third_sort = sorted(li_third, reverse=True)
if len(li) >= 2:
  if li_third_sort[0][0] == li_third_sort[1][0]:
    third = li_third_sort[1][1]
  else:
    third = li_third_sort[0][1]
else:
  third = li_third_sort[0][1]


first = round(sum(li)/len(li))
second = li[round(len(li)/2)]
four = max(li) - min(li)

print(first)
print(second)
print(third)
print(four)