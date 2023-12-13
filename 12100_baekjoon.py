# https://www.acmicpc.net/problem/12100
# 추가 고려 해야 하는 것 1. 다른 숫자를 만났을때, 2. 숫자를 만나지 못했을떄
def turn(graph, k):
    if k == 0: # right
        for i in range(n):
            x = -1
            y = -1
            px = i
            py = n-1
            for j in range(n-1, -1, -1):
                if(x==-1 and y == -1 and graph[i][j] != 0): # 숫자를 탐색
                    x = i
                    y = j
                elif(x != -1 and graph[x][y] == graph[i][j]): # 같은 숫자 합치기
                    tmp = graph[i][j] * 2
                    graph[i][j] = 0
                    graph[x][y] = 0
                    graph[px][py] = tmp
                    x = -1
                    y = -1
                    py -= 1
                elif(x != -1 and graph[i][j] != 0 and graph[x][y] != graph[i][j]):
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    graph[px][py] = tmp
                    x = i
                    y = j
                    py -= 1
            if( x != -1):
                tmp = graph[x][y]
                graph[x][y] = 0
                graph[px][py] = tmp
    elif k == 1: # up
        for i in range(n):
            x = -1
            y = -1
            px = 0
            py = i
            for j in range(n):
                if(x==-1 and y == -1 and graph[j][i] != 0):
                    x = j
                    y = i
                elif(x != -1 and graph[x][y] == graph[j][i]):
                    tmp = graph[j][i] * 2
                    graph[x][y] = 0
                    graph[j][i] = 0
                    graph[px][py] = tmp
                    x = -1
                    y = -1
                    px += 1
                elif(x != -1 and graph[j][i] != 0 and graph[x][y] != graph[j][i]):
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    graph[px][py] = tmp
                    x = j
                    y = i
                    px += 1
            if(x != -1):
                tmp = graph[x][y]
                graph[x][y] = 0
                graph[px][py] = tmp
    elif k == 2: # left
        for i in range(n):
            x = -1
            y = -1
            px = i
            py = 0
            for j in range(n):
                if(x==-1 and y == -1 and graph[i][j] != 0): # 숫자를 탐색
                    x = i
                    y = j
                elif(x != -1 and graph[x][y] == graph[i][j]): # 같은 숫자 합치기
                    tmp = graph[i][j] * 2
                    graph[i][j] = 0
                    graph[x][y] = 0
                    graph[px][py] = tmp
                    x = -1
                    y = -1
                    py += 1
                elif(x != -1 and graph[i][j] != 0 and graph[x][y] != graph[i][j]):
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    graph[px][py] = tmp
                    x = i
                    y = j
                    py += 1
            if( x != -1):
                tmp = graph[x][y]
                graph[x][y] = 0
                graph[px][py] = tmp
    elif k == 3: # down
        for i in range(n):
            x = -1
            y = -1
            px = n-1
            py = i
            for j in range(n-1, -1, -1):
                if(x==-1 and y == -1 and graph[j][i] != 0):
                    x = j
                    y = i
                elif(x != -1 and graph[x][y] == graph[j][i]):
                    tmp = graph[j][i] * 2
                    graph[x][y] = 0
                    graph[j][i] = 0
                    graph[px][py] = tmp
                    x = -1
                    y = -1
                    px -= 1
                elif(x != -1 and graph[j][i] != 0 and graph[x][y] != graph[j][i]):
                    tmp = graph[x][y]
                    graph[x][y] = 0
                    graph[px][py] = tmp
                    x = j
                    y = i
                    px -= 1
            if(x != -1):
                tmp = graph[x][y]
                graph[x][y] = 0
                graph[px][py] = tmp

def find(graph):
    m = 0
    for i in graph:
        m = max(max(i), m)
    return m

from copy import deepcopy

n = int(input())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
# 0 right 1 up 2 left 3 down

# turn(graph, 3)
# for i in graph:
#     print(i)

result = find(graph)
for a in range(4):
    g1 = deepcopy(graph)
    turn(g1, a)
    result = max(find(g1), result)
    for b in range(4):
        g2 = deepcopy(g1)
        turn(g2, b)
        result = max(find(g2), result)
        for c in range(4):
            g3 = deepcopy(g2)
            turn(g3, c)
            result = max(find(g3), result)
            for d in range(4):
                g4 = deepcopy(g3)
                turn(g4, d)
                result = max(find(g4), result)
                for e in range(4):
                    g5 = deepcopy(g4)
                    turn(g5, e)
                    result = max(find(g5), result)
print(result)