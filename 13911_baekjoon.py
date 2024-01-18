import sys
from heapq import heappush, heappop

def dijk(graph, start):
    distance = [INF] * (V+3)
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if(cost < distance[i[0]]):
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance


input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
'''
주요 아이디어
전체 맥도날드를 0의 비용으로 잇는 노드를 생성
전체 스타벅스를 0의 비용으로 잇는 노드를 생성
'''
graph = [[] for _ in range(V+3)]  #  V+1는 맥날 V+2는 스벅 엣지 0 

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

M, X = map(int, input().split())  #  맥도날드 수, 최대 맥도날드 거리
mc = list(map(int, input().split()))
S, Y = map(int, input().split())  #  스타벅스 수, 최대 스타벅스 거리
star = list(map(int, input().split()))
possible = [True] * (V+1)

for i in mc:
    graph[V+1].append([i, 0])
    possible[i] = False
for i in star:
    graph[V+2].append([i, 0])
    possible[i] = False

mc_d = dijk(graph, V+1)
star_d = dijk(graph, V+2)

#print('mc', mc_d[1:V+1])
#print('st', star_d[1:V+1])

r = INF
for i in range(1, V+1):
    if(possible[i]):
        if(mc_d[i] <= X and star_d[i] <= Y):
            r = min(r, mc_d[i] + star_d[i])

if(r == INF):
    print(-1)
else:
    print(r)