#2108
import sys
import heapq
input = sys.stdin.readline

n = int(input())

min_n = 4001
max_n = -4001

s = 0
c_minus = [0] * (4001)
c_plus = [0] * 4001

q = []

for _ in range(n):
    num = int(input())
    if(num < min_n):
        min_n = num
    if(num > max_n):
        max_n = num
    s += num
    if(num < 0):
        c_minus[abs(num)] += 1
    else:
        c_plus[num] += 1
    heapq.heappush(q, num)


a = 0

m_cnt = max(max(c_minus), max(c_plus))

cnt = 0
for i in range(4000, 0, -1):
    if(c_minus[i] == m_cnt):
        if(cnt == 1):
            a = -i
            cnt += 1
            break
        else:
            a = -i
            cnt += 1
if(cnt < 2):
    for i in range(4001):
        if(c_plus[i] == m_cnt):
            if(cnt == 1):
                a = i
                break
            else:
                a = i
                cnt += 1

for _ in range(n//2+1):
    r = heapq.heappop(q)
                
print(round(s/n))
print(r)
print(a)
print(max_n - min_n)