import sys

input = sys.stdin.readline
CONST = 1000000000

N = int(input())
poses = []

for _ in range(N):
    arr = list(map(int, input().split()))
    poses.append(arr)

poses.sort(key=lambda x: (x[0], x[1]))
s, e = poses[0]

result = 0
for i in range(1, N):
    a, b = poses[i]

    if(s <= a <= e):
        if(b >= e):
            e = b
        else:
            continue
    elif(a > e):
        result += (e-s)
        s = a
        e = b

result += (e-s)
print(result)