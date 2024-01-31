import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def dfs(x, y, graph, visited):
    command = graph[x][y]

    dx = x + move[command][0]
    dy = y + move[command][1]
    
    if(dx < 0 or dx >= N or dy < 0 or dy >= M or visited[dx][dy] == 1):
        return True
    elif(visited[dx][dy] == 0):
        return False
    elif(visited[dx][dy] == 2):
        visited[dx][dy] = 0
        if(dfs(dx, dy, graph, visited)):
            visited[dx][dy] = 1
            return True
        else:
            return False


N, M = map(int, input().split())

graph = []

for _ in range(N):
    line = list(input().strip())
    graph.append(line)

visited = [[2] * M for _ in range(N)]  # 2 : 미 방문, 0 방문, 1 탈출 가능

for x in range(N):
    for y in range(M):
        if visited[x][y] == 2:
            visited[x][y] = 0
            if dfs(x, y, graph, visited):
                visited[x][y] = 1
result = 0            
for i in visited:
    result += sum(i)
print(result)