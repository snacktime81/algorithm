from collections import Counter

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

tmp = []

for i in range(N):
    now = A[i]
    tmp.append(now)
    for j in range(i+1, N):
        now += A[j]
        tmp.append(now)

ca = dict(Counter(tmp))

tmp = []

for i in range(M):
    now = B[i]
    tmp.append(now)
    for j in range(i+1, M):
        now += B[j]
        tmp.append(now)

cb = dict(Counter(tmp))

result = 0
for i in ca:
    try:
        result += ca[i] * cb[T-i]
    except:
        continue
print(result)
