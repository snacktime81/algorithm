import heapq
n = int(input())

arr = []

for _ in range(n):
    heapq.heappush(arr, int(input()))


r = 0
if(n == 1):
    print(0)
else:
    while len(arr) > 1:
        tmp = heapq.heappop(arr) + heapq.heappop(arr)
        r += tmp
        heapq.heappush(arr, tmp)
    print(r)
    
    