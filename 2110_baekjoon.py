import sys
input = sys.stdin.readline

N, C = map(int, input().split())

arr = []

for _ in range(N):
    x = int(input())
    arr.append(x)
arr.sort()

start = 1
end = arr[N-1] - arr[0]

while start <= end:
    mid = (start + end) // 2
    first = arr[0]
    cnt = 1
    for i in arr:
        if ( i >= first + mid):
            cnt += 1
            first = i
            
    if(cnt >= C):
        start = mid + 1
        r = mid
    elif(cnt < C):
        end = mid - 1
print(r)