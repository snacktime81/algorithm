# https://www.acmicpc.net/problem/16118

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드수, 엣지 수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split()) # 노드1, 노드2, 비용
    graph[a].append([b,c*2])
    graph[b].append([a,c*2])

q = [] # heap
distance_wolf= [[INF, INF] for _ in range(n+1)]
distance_wolf[1][1] = 0

heappush(q, (0,1,True)) # True == even, False == odd

while q:
    dist, now, check = heappop(q)
    if(distance_wolf[now][check] < dist):
        continue
    elif(distance_wolf[now][not check] < dist):
        continue
    
    for i in graph[now]:
        if(check): # 홀수번 움직일 차례
            cost = dist + (i[1] // 2)
        else:
            cost = dist + (i[1] * 2)
        
        if( cost < distance_wolf[i[0]][not check]):
            heappush(q, (cost, i[0], not check))
            distance_wolf[i[0]][not check] = cost

q = []
distance_fox = [INF for _ in range(n+1)]
heappush(q, (0,1))
distance_fox[1] = 0
while q:
    dist, now = heappop(q)
    if( distance_fox[now] < dist):
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if(cost < distance_fox[i[0]]):
            distance_fox[i[0]] = cost
            heappush(q, (cost, i[0]))
    
#print(distance_wolf)
#print(distance_fox)
answer = 0
for i in range(2, n+1):
    wolf1, wolf2 = distance_wolf[i]
    fox = distance_fox[i]
    
    if(fox < wolf1 and fox < wolf2):
        answer += 1
print(answer)