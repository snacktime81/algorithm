from collections import deque

N, k = map(int, input().split())
num = list(map(int ,input()))
num = deque(num)

q = []
l = 0
st_l = N-k

while num:
    n = num.popleft()
    if not q or k == 0:
        q.append(n)
        l += 1
        continue
    else:
        while q and q[-1] < n and k > 0:
            q.pop()
            k -= 1
            l -= 1
    q.append(n)
    l += 1
while l > st_l:
    l -= 1
    q.pop()
for i in q:
    print(int(i), end='')