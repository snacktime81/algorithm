from collections import deque


def bfs(graph, coordinate, X, Y):

    move = [(0, -1), (0, 1), (1, 0), (-1, 0)] 
    
    q = deque()
    
    for i in coordinate:
        q.append((i[0], i[1], 0))
    max_d = 0
    while q:
        x, y, d = q.popleft()
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            dd = d + 1
            
            if( dx < 0 or dy < 0 or dx >= X or dy >= Y ):
                continue

            if(graph[dy][dx] == 0):
                q.append((dx,dy,dd))
                if(dd > max_d):
                    max_d = dd
                graph[dy][dx] = 1
    return(graph, max_d)


    
x, y = map(int, input().split())
graph = []
for _ in range(y):
    graph.append(list(map(int, input().split())))

coordinate = []

for i in range(len(graph)):
    for j in range(len(graph[i])):
            if(graph[i][j] == 1):
                coordinate.append([j,i])

g, m = bfs(graph,coordinate, x, y)



check = False
for i in graph:
    for j in i:
        if(j == 0):
            print(-1)
            check = True
            break
    if(check):
        break
            
else:
    print(m)

        
