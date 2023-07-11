#1260

import sys
from collections import deque

n, m, v = map(int, input().split())

arr = [ [] for _ in range(n+1)]
visitedDfs = [False for _ in range(n+1)]
visitedBfs = [False for _ in range(n+1)]

for _ in range(m):
    startNode, endNode = map(int, input().split())
    
    arr[startNode].append(endNode)
    arr[endNode].append(startNode)

def dfs(arr, start, visited):
    
    visited[start] = True
     
    print(start, end=' ')
    
    tmp = arr[start] if arr[start] != None else []
    tmp.sort()
    
    for i in arr[start]:
        if not visited[i]:
            dfs(arr,i, visited)
            
def bfs(arr, start, visited):
    
    queue = deque([start])
    
    visited[start] = True
    print(start, end=' ')
    while queue:
        node = queue.popleft()
        
        tmp = arr[node] if arr[node] != None else []
        tmp.sort()
        for i in tmp:
            if not visited[i]:
                queue.append(i)
                print(i, end=' ')
                visited[i] = True
dfs(arr, v, visitedDfs)
print()
bfs(arr, v, visitedBfs)