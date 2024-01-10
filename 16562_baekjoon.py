INF = int(1e9)

n, m, k = map(int, input().split())
friend_fees = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]
fees = [INF] * (n+1)


def find(x, parent):
    if(x != parent[x]):
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b
        
        
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b, parent)

for i in range(n+1):
    find(i, parent)
    
for i in range(n+1):
    root = parent[i]
    fees[root] = min(fees[root], friend_fees[i])

r = 0
cnt = 0
c = [False] * (n+1)
for i in range(1, n+1):
    fee = fees[i]
    if(fee != INF and not c[parent[i]]):
        r += fee
        cnt += 1
        c[parent[i]] = True

if(k >= r):
    print(r)
else:
    print('Oh no')