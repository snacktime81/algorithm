import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

minus = []
plus = []

for _ in range(n):
    num = int(input())

    if(num <= 0):
        heappush(minus, num)
    else:
        heappush(plus, -num)

r = 0

while len(minus) >= 2:
    v1 = heappop(minus)
    v2 = heappop(minus)
    r += (v1 * v2)

while minus:
    r += heappop(minus)

while len(plus) >= 2:
    v1 = heappop(plus)
    v2 = heappop(plus)

    if(v1 == -1 or v2 == -1):
        r -= (v1 + v2)
        continue
    r += (v1 * v2)
while plus:
    r -= heappop(plus)
print(r)