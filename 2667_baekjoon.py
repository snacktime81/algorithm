#2667
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = []



for i in range(n):
    line = list(map(int, input().rstrip()))
    arr.append(line)
    
move = [(0,1), (0,-1), (1,0), (-1,0)]
result = 0

def bfs(arr, start, n):
    que = deque([start])
    
    x, y = start
    
    if(arr[x][y] == 0):
        return [False, 0]
    cnt = 0  
    while que:
        x, y = que.popleft()

        if(arr[x][y] == 1):
            arr[x][y] = 0
            cnt += 1
            for i in move:
                dx = x + i[0]
                dy = y + i[1]
                if(dx < 0 or dy < 0 or dx >= n or dy >= n):
                    continue
                if(arr[dx][dy] == 1):
                    que.append((dx,dy))
                    

    return [True, cnt]

            
cnt = 1
arrT = []

for i in range(n):
    for j in range(n):
        tmp = bfs(arr, (i,j), n)
        if(tmp[0]):
            result += 1
            arrT.append(tmp[1])
            
print(result)
arrT.sort()
for i in arrT:
    print(i)