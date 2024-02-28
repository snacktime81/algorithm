from heapq import heappush, heappop

N, M = map(int, input().split())

depend = [0]*(N+1)
g = [[] for _ in range(N+1)]

q = []
for _ in range(M):
    a, b = map(int, input().split())
    depend[b] += 1
    g[a].append(b)
for i in range(1, N+1):
    if depend[i] == 0:
        heappush(q, i)

while q:
    node = heappop(q)
    print(node, end=' ')
    for i in g[node]:
        depend[i] -= 1
        if depend[i] == 0:
            heappush(q, i)

