# https://www.acmicpc.net/problem/1005

import sys
from collections import deque


INF = int(1e9)

T = int(input())

for _ in range(T):

    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    
    depend = [0 for _ in range(n+1)]
    distance = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        
        depend[b] += 1
        graph[a].append(b)
        
    w = int(input())
    

    q = deque()
    for i in range(1, n+1): # 초기 의존도 검사
        if(depend[i] == 0):
            q.append(i)
            distance[i] = costs[i-1]
    
    while q: # 초기 건물 부터 지을 수 있는 건물들을 조사
        node = q.popleft()
        for j in graph[node]:
            depend[j] -= 1
            distance[j] = max(distance[j], costs[j-1] + distance[node])
            
            if(depend[j] == 0):
                q.append(j)

    
    print(distance[w])