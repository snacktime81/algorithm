#https://www.acmicpc.net/problem/4883

import sys
input = sys.stdin.readline

move = [[(-1,1),(-1,0)],[(-1,-1),(-1,0),(-1,1),(0,-1)],[(-1,-1),(-1,0),(0,-1)]]
case = 1
while True:
    n = int(input())
    if(n == 0):
        break
    graph = []
    
    for _ in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        
    graph[1][0] += graph[0][1]
    graph[0][2] += graph[0][1]
    graph[1][1] += min(graph[0][1], graph[1][0], graph[0][2]) # 비용이 음수일 수도 있다
    graph[1][2] += min(graph[0][1], graph[1][1], graph[0][2])
    
    for i in range(2, n):
        for j in range(3):
            sets = []
            for x,  y in move[j]:
                sets.append(graph[i+x][j+y])
            graph[i][j] += min(sets)
    print(f'{case}. {graph[n-1][1]}')
    case += 1