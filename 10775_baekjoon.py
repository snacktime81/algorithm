#https://www.acmicpc.net/problem/10775

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


G = int(input())
P = int(input())

#gates = [0] * (G+1)
gates = [i for i in range(G+1)]
r = 0
check = False
for i in range(1, P+1):
    gate = int(input())
    if(not check):
        if(gates[gate] == gate):
            union(gate, gate-1, gates)
            r += 1
        else:
            tmp = find(gate, gates)
            if(tmp != 0):
                union(tmp, tmp-1, gates)
                r += 1
            else:
                check = True
                continue
print(r)