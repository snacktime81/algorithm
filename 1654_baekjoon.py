k, N = map(int, input().split())


lens = []
for _ in range(k):
    l = int(input())
    lens.append(l)
s = 1
e = max(lens)

while s <= e:
    cnt = 0
    mid = (s+e)//2
    for l in lens:
        cnt += (l//mid)
    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1
print(e)