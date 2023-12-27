# https://www.acmicpc.net/problem/17619

import sys
input = sys.stdin.readline

def find(x, p):
    if(p[x] != x):
        p[x] = find(p[x], p)
    return p[x]

def union(a, b, p):
    a = find(a, p)
    b = find(b, p)
    if(a<b):
        p[b] = a
    else:
        p[a] = b

n, q = map(int, input().split())

logs = []

for i in range(1, n+1):
    x1, x2, y = map(int, input().split())
    
    logs.append([x1,x2,y,i])

logs.sort(key = lambda x:x[0])

parents = [i for i in range(n+1)]

s = logs[0][0]
e = logs[0][1]
node = logs[0][3]

for i in range(1, n):
    now_s = logs[i][0]
    now_e = logs[i][1]
    now_node = logs[i][3]
    if(s<=now_s<=e):
        union(now_node, node, parents)
    if(now_e >= e):
        s = now_s
        e = now_e
        node = now_node
for i in range(q):
    a, b = map(int, input().split())
    a = find(a, parents)
    b = find(b, parents)
    if(a == b):
        print(1)
    else:
        print(0)
        
    
    