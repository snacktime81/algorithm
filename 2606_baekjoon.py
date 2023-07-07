# 2606
import sys
from collections import deque

c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph = [[] for _ in range(c+1)]
visited = [False] * (c+1)

for _ in range(n):
    computer, link = map(int, sys.stdin.readline().split())
    #print(link)
    graph[computer].append(link)
    graph[link].append(computer)
    
def bfs(graph, node, visited):
    if visited[node]:
        return False
    
    visited[node] = True
    queue = deque([node])
    
    while queue:
        
        computer = queue.popleft()
        for i in graph[computer]:
            
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
    return visited
virus = bfs(graph, 1, visited)

answer = 0

for i in virus:
    if(i):
        answer += 1
        
print(answer-1)
        