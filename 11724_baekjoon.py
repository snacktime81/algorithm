import sys
from collections import deque

input = sys.stdin.readline



n, m = map(int, input().split())

arr = [ [] for i in range(n+1) ]
visited = [False for i in range(n+1)]

for i in range(m):
    
    node, edge = map(int, input().split())
    
    arr[node].append(edge)
    #arr[edge].append(node)
    

def bfs(arr, node):
    queue = deque([node])
    
    if visited[node]:
        return False
    
    while queue:

        node = queue.popleft()

        visited[node] = True

        for i in arr[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return True

result = 0
for i in range(1, n+1):
    if (bfs(arr, i)):
        result += 1
print(result)
