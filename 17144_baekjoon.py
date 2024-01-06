from copy import deepcopy

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C, T = map(int ,input().split())
graph = []
machine = []

def spread(graph, R, C):
    tmp = deepcopy(graph)
    
    for i in range(R):
        for j in range(C):
            if(graph[i][j] != 0 and graph[i][j] != -1):
                div = graph[i][j] // 5
                for k in move:
                    dx = i + k[0]
                    dy = j + k[1]
                    if( 0 <= dx < R and 0 <= dy < C and graph[dx][dy] != -1):
                        tmp[dx][dy] += div
                        tmp[i][j] -= div
    return tmp

def turn(graph, R, C, machine):
    x1, y1 = machine[0]
    x2, y2 = machine[1]
    
    t1 = graph[x1][1]
    graph[x1][1] = 0
    for i in range(2, C):
        t2 = graph[x1][i]
        graph[x1][i] = t1
        t1 = t2
    
    for i in range(x1-1, -1, -1):
        t2 = graph[i][C-1]
        graph[i][C-1] = t1
        t1 = t2
    
    for i in range(C-2, -1, -1):
        t2 = graph[0][i]
        graph[0][i] =t1
        t1 = t2
    
    for i in range(1, x1):
        t2 = graph[i][0]
        graph[i][0] = t1
        t1 = t2
        
    #--------------------------------
    t1 = graph[x2][1]
    graph[x2][1] = 0
    for i in range(2, C):
        t2 = graph[x2][i]
        graph[x2][i] = t1
        t1 = t2
    
    for i in range(x2+1, R):
        t2 = graph[i][C-1]
        graph[i][C-1] = t1
        t1 = t2
    
    for i in range(C-2, -1, -1):
        t2 = graph[R-1][i]
        graph[R-1][i] = t1
        t1 = t2

    for i in range(R-2, x2, -1): # 5 3
        t2 = graph[i][0]
        graph[i][0] = t1
        t1 = t2

for i in range(R):
    line = list(map(int, input().split()))
    graph.append(line)
    
    for j in range(C):
        if(line[j] == -1):
            machine.append([i, j])

r = 2
for _ in range(T):
    graph = spread(graph, R, C)
    turn(graph, R, C, machine)
    

for i in graph:
    r += sum(i)


print(r)
