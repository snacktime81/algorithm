import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [ ]

for _ in range(n):
    graph.append(list(map(int, input().split())))

movel = [(0, 1), (0, 2), (0, 3)]
moveO = [(0, 1), (1, 0), (1, 1)]
moveT = [(0, 1), (0, 2), (1, 1)]
moveL = [(1, 0), (2, 0), (2, 1)]
moveS = [(1, 0), (1, 1), (2, 1)]
moveJ = [(1, 0), (2, 0), (2, -1)]
moveZ = [(1, 0), (1, -1), (2, -1)]

moveAll = [movel, moveO, moveT, moveL, moveJ, moveS, moveZ]

# 4 5

# 0 0 -> 0 4
# 0 1 -> 1 4
# 0 2 -> 2 4
# 0 3 -> 3 4
# 0 4 -> 4 4

# 5번 반복

# 5 4


def turn(graph):
    
    n = len(graph)
    m = len(graph[0])

    g = [[] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            g[i].append(graph[j][m-1-i])
    return g
    
    
def tetromino(start, graph):
    
    maxSum = 0
    
    n = len(graph)
    m = len(graph[0])
    
    
    for move in moveAll:
        
        check = False
        
        blockCoor = [] # 테트로미노 4개의 조각의 좌표
        
        for i in move:
            blockCoor.append( (start[0] + i[0], start[1] + i[1]) )
        
        
        blockCoor.append( (start[0], start[1]) )
        
        s = 0 # sum
        
        for coorSet in blockCoor:
            x = coorSet[0]
            y = coorSet[1]
            
            if(x < 0 or y < 0 or x >= n or y >= m):
                check = True
                break
                
            s += graph[x][y]
            
        if(check):
            continue
        
        # if(move == moveJ):
        #     print(s)
        #     print(blockCoor)
        #     print(graph)
        
        if(s > maxSum):
            maxSum = s

    return maxSum

maxSum = 0

for _ in range(4):
    
    #print(graph)
    
    n = len(graph)
    m = len(graph[0])
    
    for i in range(n):
        for j in range(m):
            s = tetromino((i, j), graph)
            if( s > maxSum):
                maxSum = s
                
    graph = turn(graph)
    

    
print(maxSum)