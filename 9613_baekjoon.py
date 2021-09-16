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
  nums.pop(0)
  gcd_sum = 0
  for i in range(len(nums) - 1):
    num_index = nums.index(nums[i])
    for j in range(num_index+1, len(nums)):
      if nums[i] > nums[j]:
        gcd_sum += gcd(nums[i], nums[j])
      elif nums[i] < nums[j]:
        gcd_sum += gcd(nums[j], nums[i])
      else:
        gcd_sum += nums[i]
  print(gcd_sum)
