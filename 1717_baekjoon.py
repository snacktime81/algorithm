# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def find(x, p):
    if(p[x] != x):
        p[x] = find(p[x], p)
    return p[x]

def union(a, b, p):
    a = find(a, sets)
    b = find(b, sets)
    if(a<b):
        p[b] = a
    else:
        p[a] = b

n, m = map(int, input().split())

sets = [i for i in range(n+1)]

for _ in range(m):
    c, a, b= map(int, input().split())
    if(c == 0):
        union(a,b,sets)
    else:
        a = find(a, sets)
        b = find(b, sets)
        if(a==b):
            print('yes');
        else:
            print('no')