import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def check(team, graph):
    visited = [False] * (N+1)
    
    start = team[0]
    q = deque([start])
    visited[start] = True
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if( i in team and not visited[i]):
                q.append(i)
                visited[i] = True
    c = True
    for node in team:
        if not visited[node]:
            c = False
            break
    return c
    

N = int(input())
PEOPLE = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

data = [i for i in range(1, N+1)]

for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(1, line[0]+1):
        graph[i].append(line[j])
result = INF
for i in range(1, N):
    team = list(combinations(data, i))

    for a in team:
        b = []
        for j in data:
            if(j not in a):
                b.append(j)
            
        if not check(a, graph):
            continue
        if not check(b, graph):
            continue
        people_a = 0
        people_b = 0
        for i in a:
            people_a += PEOPLE[i]
        for i in b:
            people_b += PEOPLE[i]
        result = min(result, abs(people_a-people_b))

if(result == INF):
    print(-1)
else:
    print(result)