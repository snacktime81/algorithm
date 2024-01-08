 # 1931

import sys

input = sys.stdin.readline

n = int(input())
arr = []

check = dict()

pre = 0

for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    check[a] = 0
    check[b] = 0
arr.sort(key=lambda x: (x[1], x[0]))
endpoint = 0
for i in arr:
    start, end = i
    
    if(start >= endpoint):
        check[end] = pre+1
        endpoint = end
    else:
        check[end] = pre
    pre = check[end]
    
print(check[end])
