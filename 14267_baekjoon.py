import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

points = [0] * (N + 1)

for _ in range(M):
    officer, point = map(int, input().split())
    points[officer] += point
for i in range(2, N+1):
    up = arr[i]
    if(up == -1):
        continue
    points[i] += points[up]
for i in range(1, N+1):
    print(points[i], end=' ')