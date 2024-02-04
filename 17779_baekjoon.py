import sys

input = sys.stdin.readline

def find_minimum_diff(graph, x, y, d1, d2):
    result = [0, 0, 0, 0, 0, 0]

    visited = [[0] * N for _ in range(N)]

    for i in range(d1+1):
        dx = x + i
        dy = y - i
        visited[dx][dy] = 5

        dx = x + d2 + i
        dy = y + d2 - i
        visited[dx][dy] = 5

    for i in range(d2+1):
        dx = x + i
        dy = y + i
        visited[dx][dy] = 5

        dx = x + d1 + i
        dy = y - d1 + i
        visited[dx][dy] = 5
    
    for i in range(N):
        check = False
        for j in range(N):
            if(i == x and j == y ) or (i == x+d1+d2 and j == x-d1+d2):
                break
            if visited[i][j]:
                check = not check
            elif(check):
                visited[i][j] = 5
    # sector 1     
    for i in range(x+d1):
        for j in range(y+1):
            if(visited[i][j]):
                continue
            visited[i][j] = 1
            result[1] += graph[i][j]
    
    # sector 2
    for i in range(x+d2+1):
        for j in range(y+1, N):
            if(visited[i][j]):
                    continue
            visited[i][j] = 2
            result[2] += graph[i][j]
    
    # sector 3
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if(visited[i][j]):
                continue
            visited[i][j] = 3
            result[3] += graph[i][j]
    
    #sector 4
    for i in range(x+d2, N):
        for j in range(y-d1+d2, N):
            if(visited[i][j]):
                continue
            visited[i][j] = 4
            result[4] += graph[i][j]
    
    for i in range(N):
        for j in range(N):
            if(visited[i][j] == 5):
                result[5] += graph[i][j]
    
    val = max(result[1:]) - min(result[1:])
    return val


N = int(input())
graph = []
for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

result = int(1e9)
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if(x+d1+d2 >= N or y+d2 >= N or y-d1 < 0):
                    break
                elif(y+d2 >= N):
                    break
                result = min(result, find_minimum_diff(graph, x,y,d1,d2))
print(result)
                    
                