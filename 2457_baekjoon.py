import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

N = int(input())

arr = []

cnt = 0
end = 0

for _ in range(N):
    m1, d1, m2, d2 = map(int, input().split())
    s = m1*100 + d1
    e = m2*100 + d2
    arr.append([s, e])

arr.sort(key=lambda x: (x[0], x[1]))
arr = deque(arr)
arr.append([-1,-1])

end = 0
next = 0
while arr:
    s, e = arr.popleft()
    #print(s, e, end, next)
    if next >= 1201:
        cnt += 1
        end = next
        break

    if s == -1 and e == -1:
        break

    if len(arr) == 0 and next < 1201:
        cnt = 0
        break

    if s <= 301 and e > 301:
        end = max(e, end)
        cnt = 1
    elif s <= end:
        next = max(next, e, end)
    elif s > next and end != 0:
        cnt = 0
        break
    elif s > end and end != 0:
        end = next
        next = 0
        if s <= end:
            next = max(end, e)
        cnt += 1
    if end >= 1201:
        break
if end < 1201:
    cnt = 0

print(cnt)