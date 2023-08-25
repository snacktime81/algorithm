import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

INF = int(1e9)

graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dij(start, des, graph): # 출바점, 도착점, edge
    
    cost = [INF for _ in range(n+1)]
    
    q = []
    
    heapq.heappush(q, (0, start))
    cost[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if(cost[now] < dist):
            continue
        
        for i in graph[now]:
            c = dist + i[1]
            
            if c < cost[i[0]]:
                cost[i[0]] = c
                heapq.heappush(q, (c, i[0]))

    return cost[des]

result = []

for i in range(1, n+1):
    cost = dij(i, x, graph)
    cost += dij(x, i, graph)
    result.append(cost)
print(max(result))
    
    
    