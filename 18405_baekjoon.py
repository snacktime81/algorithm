import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int ,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
s, tx, ty = map(int, input().split())
move = [(0,1), (0, -1), (-1, 0), ( 1, 0)]

x, y =(0,0)

q = deque([x, y])

def bfs(graph, start):
    for i in range(1, k+1):
        for x in range(n):
            for y in range(n):
                if(graph[x][y] == i):
                    for j in move:
                        dx = x + j[0]
                        dy = y + j[1]
                        if((dx < 0 or dy < 0 or dx >=n  or dy >= n) or graph[dx][dy] < 0):
                            continue
                        graph[dx][dy] = i*(-1)
                        
def change(graph, k):
    for x in range(n):
        for y in range(n):
            if(graph[x][y] < 0):
                graph[x][y] *= -1
    

for _ in range(s):
    bfs(graph, (0,0))
    change(graph, k)

print(graph[tx-1][ty-1])