from collections import deque

n, m = map(int, input().split())

q = deque([(m, 0)])
d = [10000000] * (100000 * 2)
d[m] = 0
while q:
    now, dist = q.popleft()
    
    if(now == n):
        print(dist)

    e = now - 1
    if(e >= 0 and d[e] > dist+1):
        d[e] = dist+1
        q.append([e, dist+1])
    
    e = now + 1
    if(e < 100000*2 and d[e] > dist+1):
        d[e] = dist+1
        q.append([e, dist+1])
    
    if(now % 2 == 0 and d[now//2] > dist + 1):
        e = now // 2
        d[e] = dist+1
        q.append([e, dist+1])