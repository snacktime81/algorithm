import sys

input = sys.stdin.readline


def find(x, p):
    if p[x] != x:
        p[x] = find(p[x], p)
    return p[x]


def union(a, b, p):
    a = find(a, p)
    b = find(b, p)

    if a < b:
        p[b] = a
    else:
        p[a] = b

T = int(input())

for num in range(T):
    n = int(input())
    k = int(input())
    parent = [i for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b, parent)

    m = int(input())
    print(f'Scenario {num+1}:')
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a, parent) == find(b, parent):
            print(1)
        else:
            print(0)
    print()