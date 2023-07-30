from collections import deque


def bfs(graph, coordinate, X, Y, Z):

    move = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)] 
    
    q = deque()
    
    for i in coordinate:
        q.append((i[0], i[1], i[2], 0))
    max_d = 0
    while q:
        x, y, z, d = q.popleft()
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            dz = z + i[2]
            dd = d + 1
            
            if( dx < 0 or dy < 0 or dz < 0 or dx >= X or dy >= Y or dz >= Z):
                continue

            if(graph[dz][dy][dx] == 0):
                q.append((dx,dy,dz, dd))
                if(dd > max_d):
                    max_d = dd
                graph[dz][dy][dx] = 1
    return(graph, max_d)


    
x, y, z = map(int, input().split())
graph = [[] for _ in range(z)]
for i in range(z):
    for _ in range(y):
        graph[i].append(list(map(int, input().split())))


coordinate = []

for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if(graph[i][j][k] == 1):
                coordinate.append([k,j,i])

g, m = bfs(graph,coordinate, x, y ,z)

check = False
for i in graph:
    for j in i:
        for k in j:
            if(k == 0):
                print(-1)
                check = True
                break
        if(check):
            break
    if(check):
        break
        
            
else:
    print(m)

        
