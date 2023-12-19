import sys
from collections import deque
input = sys.stdin.readline
    
n, m = map(int, input().split())

depend = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    depend[b] += 1
    graph[a].append(b)
    
q = deque()

for i in range(1, n+1):
    if(depend[i] == 0):
        q.append(i)
        
while q:
    num = q.popleft()
    print(num, end=' ')
    for i in graph[num]:
        depend[i] -= 1
        if(depend[i] == 0):
            q.append(i)