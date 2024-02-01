import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
parent = [0] * N
graph = [[] for _ in range(N)]

for i in range(N):
    person = arr[i]
    if(person == -1):
        continue
    graph[person].append(i)
    parent[person] += 1


dp = [-1] * (N)

def dfs(node):
    result = 0
    tmp = []
    
    for i in graph[node]:
        time = dfs(i)
        tmp.append([time, i])
    cost = 1
    tmp.sort(reverse=True)
    for i in tmp:
        result = max(result, i[0] + cost)
        cost += 1
    #print(node, result)
    return result

print(dfs(0))