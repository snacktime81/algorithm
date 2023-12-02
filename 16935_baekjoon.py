import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

def f1(graph):
    tmp = [[] for _ in range(n)]
    for i in range(n):
        tmp[n-1-i] = graph[i]
    return tmp

def f2(graph):
    tmp = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            tmp[j][i] = graph[j][m-i-1]
    return tmp

def f3(graph):
    tmp = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp[j][n-i-1] = graph[i][j]
    return tmp

def f4(graph):
    tmp = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp[m-j-1][i] = graph[i][j]
    return tmp

def f5(graph):
    tmp = [[0] * m for _ in range(n)]
    k = n//2
    l = m//2
    
    for i in range(4):
        if(i == 0):
            for x in range(k):
                for y in range(l):
                    tmp[x][y] = graph[x+k][y]
        elif(i == 1):
            for x in range(k):
                for y in range(l, m):
                    tmp[x][y] = graph[x][y-l]
        elif(i == 2):
            for x in range(k, n):
                for y in range(l, m):
                    tmp[x][y] = graph[x-k][y]
        else:
            for x in range(k, n):
                for y in range(l):
                    tmp[x][y] = graph[x][y-l]
    return tmp

def f6(graph):
    tmp = [[0] * m for _ in range(n)]
    k = n//2
    l = m//2
    
    for i in range(4):
        if(i == 0):
            for x in range(k):
                for y in range(l):
                    tmp[x][y] = graph[x][y-l]
        elif(i == 1):
            for x in range(k):
                for y in range(l, m):
                    tmp[x][y] = graph[x+k][y]
        elif(i == 2):
            for x in range(k, n):
                for y in range(l, m):
                    tmp[x][y] = graph[x][y-l]
        else:
            for x in range(k, n):
                for y in range(l):
                    tmp[x][y] = graph[x-k][y]
    return tmp

f = [0, f1, f2, f3, f4, f5, f6]

if(r > 1):
    func = list(map(int, input().split()))
else:
    func = [int(input())]
for i in func:
    graph = f[i](graph)
    n = len(graph)
    m = len(graph[0])
    
for i in graph:
    for j in i:
        print(j, end=' ')
    print()