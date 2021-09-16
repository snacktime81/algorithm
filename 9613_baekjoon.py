#9613
import sys
n = int(sys.stdin.readline())

def gcd(big, small):
  while small > 0:
    key = big % small
    big = small
    small = key
  return big

for i in range(n):
  nums = list(map(int, sys.stdin.readline().split()))
  k = nums.pop(0)
  gcd_sum = 0
  for i in range(k):
    for j in range(k):
      if i > j:
        gcd_sum += gcd(nums[i], nums[j])
  print(gcd_sum)
