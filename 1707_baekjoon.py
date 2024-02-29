from collections import deque
import sys

input = sys.stdin.readline


def bfs(node, check, set):
    q = deque([(node, check)])  # node, 집합 번호
    while q:
        node, check = q.popleft()
        for i in g[node]:
            try:
                a = set[i]
                if a == check:
                    return False
                else:
                    continue
            except:
                set[i] = not check
                q.append([i, not check])
    return True

T = int(input())

for _ in range(T):
    v, e = map(int, input().split())
    result = 'YES'

    g = [[] for _ in range(v+1)]

    set = {1: False}

    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    bfs(1, False, set)
    for i in range(2, v):
        try:
            check = set[i]
        except:
            check = False
        if not bfs(i, check, set):
            result = 'NO'
            break

    print(result)