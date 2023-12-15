# https://www.acmicpc.net/problem/15684
import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n, m, h = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a, b = map(int ,input().split())
    graph[a-1][b-1] = 1
    graph[a-1][b] = 2

tg = deepcopy(graph)
c = []
for i in range(h):
    for j in range(n-1):
        if(tg[i][j] == 1):
            continue
        elif(tg[i][j] == 2):
            continue
        elif(tg[i][j] == 0 and tg[i][j+1] == 1):
            continue
        c.append([[i,j],[i,j+1]])
case1 = deepcopy(c)
case2 = list(combinations(c, 2))
case3 = list(combinations(c, 3))

def check(graph):
    # for i in graph:
    #     print(i)
    for i in range(n):
        y = i
        for j in range(h):
            #print('pos', j, y)
            if(graph[j][y] == 1):
                y += 1
            elif(graph[j][y] == 2):
                y -= 1

        if(y != i):
            return False
    return True

result = -1

if(check(graph)):
    print(0)
else:
    for a, b in case1:
        graph[a[0]][a[1]] = 1
        graph[b[0]][b[1]] = 2

        if(check(graph)):
            result = 1
            break
        graph[a[0]][a[1]] = 0
        graph[b[0]][b[1]] = 0
        
    if(result == -1):
        for one, two in case2:
            a, b = one
            c, d = two
            if(a == c or a == d or b == c or d == b):
                continue
            graph[a[0]][a[1]] = 1
            graph[b[0]][b[1]] = 2
            graph[c[0]][c[1]] = 1
            graph[d[0]][d[1]] = 2
            if(check(graph)):
                result = 2
                break
            graph[a[0]][a[1]] = 0
            graph[b[0]][b[1]] = 0
            graph[c[0]][c[1]] = 0
            graph[d[0]][d[1]] = 0
    if(result == -1):
        for one, two, three in case3:
            a, b = one
            c, d = two
            e, f = three
            
            if(a in two or a in three or b in two or b in three or c in three or d in three):
                continue
            graph[a[0]][a[1]] = 1
            graph[b[0]][b[1]] = 2
            graph[c[0]][c[1]] = 1
            graph[d[0]][d[1]] = 2
            graph[e[0]][e[1]] = 1
            graph[f[0]][f[1]] = 2
            if(check(graph)):
                result = 3
                break
            graph[a[0]][a[1]] = 0
            graph[b[0]][b[1]] = 0
            graph[c[0]][c[1]] = 0
            graph[d[0]][d[1]] = 0
            graph[e[0]][e[1]] = 0
            graph[f[0]][f[1]] = 0
    print(result)