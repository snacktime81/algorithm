# https://www.acmicpc.net/problem/1976

import sys

input = sys.stdin.readline

n = int(input()) # 총 도시 수
m = int(input()) # 여행 갈 도시 수

parent = [ i for i in range(n+1)]

def find(parent, target):
    if parent[target] != target:
        parent[target] =find(parent, parent[target])
    return parent[target]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if( a < b ):
        parent[b] = a
    else:
        parent[a] = b
    
for i in range(1, n+1):
    line = list(map(int, input().split()))
    
    for j in range(1, n+1):
        if(line[j-1] == 1):
            union(parent, i, j)

cities = list(map(int, input().split()))

k = parent[cities[0]]
check = True

for i in cities:
    if(k == parent[i]):
        continue
    else:
        check = False
        break

if(check):
    print("YES")
else:
    print("NO")