#11652
import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
  nums.append(int(sys.stdin.readline()))

count = {}
k = []
for i in nums:
  cnt = nums.count(i)
  try:
    if count[cnt] < i:
      continue
    else:
      count[cnt] = i
  except KeyError:
      count[cnt] = i
  k.append(cnt)

max_k = max(k)
print(count[max_k])

#count_sort = sorted(count, reverse=True, key=lambda x:x[0])
#count_sort2 = sorted(count_sort, key=lambda x:x[1])
