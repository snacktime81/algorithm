import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

move ={'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
graph = []
n, m = map(int ,input().split())

for _ in range(n):
    line = list(input().rstrip())
    graph.append(line)
    
parent_table = [i for i in range(n*m+1)]
visited = [[0] * m for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        visited[i][j] = cnt
        cnt += 1
        
def find(target):
    if(parent_table[target] != target):
        parent_table[target] = find(parent_table[target])
    return parent_table[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if( a < b ):
        parent_table[b] = a
    else:
        parent_table[a] = b
        
cnt = 0
for i in range(n):
    for j in range(m):
        dest = graph[i][j]
        parent = visited[i][j]
        dx = i + move[dest][0]
        dy = j + move[dest][1]
        child = visited[dx][dy]
        #print(parent, child)
        
        if(find(parent) == find(child)):
            cnt += 1
        union(child, parent)
        #print(parent_table)

print(cnt)

    