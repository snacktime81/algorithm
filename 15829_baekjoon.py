import sys

n = int(sys.stdin.readline())
li = sys.stdin.readline()
#hash = {}
sum = 0
# for i in range(97, 123):
#     hash[chr(i)] = (i - 96)
for i in range(n):
    sum += (ord(li[i])-96) * 31**i
print(sum % 1234567891)

