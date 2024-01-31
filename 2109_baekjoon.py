import sys

input = sys.stdin.readline


def find(x, parent):
    if(parent[x] != x):
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b


N = int(input())

data = []
last_day = 0

for _ in range(N):
    fee, day = map(int, input().split())
    data.append([fee, day])
    last_day = max(last_day, day)
data.sort(reverse=True)
costs = [0] * (last_day+1)

parent = [i for i in range(last_day+1)]

for fee, day in data:
    index = find(day, parent)
    if(costs[index] == 0 and index != 0):
        costs[index] = fee
        union(day, index-1, parent)
print(sum(costs))

