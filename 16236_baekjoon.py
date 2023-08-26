from collections import deque
import heapq
from copy import deepcopy

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
size = 2


for i in range(n):
    for j in range(n):
        if(graph[i][j] == 9):
            shark = [i, j]

visited = [[0 for _ in range(n)] for _ in range(n)]
move = [(0,1), (0,-1), (-1,0), (1,0)]



def findFish(graph, visited, shark):
    sx, sy = shark
    
    q = deque([(sx, sy)])
    
    visited[sx][sy] = 0
    
    fish = []
    
    while q:
        x, y = q.popleft()
        
        for i in move:
            dx = x + i[0]
            dy = y + i[1]
            
            if( dx < 0 or dy <0 or dx >= n or dy >= n):
                continue
            
            if( graph[dx][dy] > size or visited[dx][dy]):
                continue
            
            visited[dx][dy] = visited[x][y] + 1
            
            q.append([dx, dy])
            if(graph[dx][dy] < size and graph[dx][dy] != 0):
                heapq.heappush(fish, (visited[dx][dy], dx, dy))  

    if(len(fish) == 0):
        #print('end')
        return [0, -1, -1]
    
    if(len(fish) == 1):
        cost, ex, ey = heapq.heappop(fish)
        graph[ex][ey] = 9
        graph[sx][sy] = 0
        #print(graph)
        #print('1,', ex, ey)
        return [cost, ex, ey]

    
    cost, ex, ey = heapq.heappop(fish)
    tmp = []
    heapq.heappush(tmp, [ex, ey])
    
    while (len(fish) > 0):
        two = heapq.heappop(fish)
        
        if(cost == two[0]):
            heapq.heappush(tmp, [two[1], two[2]])
        else:
            break
    
    ex, ey = heapq.heappop(tmp)
    tmp2 = []
    heapq.heappush(tmp2, ey)
    
    while(len(tmp) > 0):
        three = heapq.heappop(tmp)
        
        if(ex == three[0]):
            heapq.heappush(tmp2, three[1])
        else:
            break
            
    ey = heapq.heappop(tmp2)
    graph[ex][ey] = 9
    graph[sx][sy] = 0
    #print(graph)
    #print('2,' ,ex, ey)
    return [cost, ex, ey]

    


cost, ex, ey = findFish(graph, deepcopy(visited), shark)
cnt = 1

total = cost



while cost > 0:
    
    if(cnt == size and size < 9):
        size += 1
        cnt = 0
    
    cost, ex, ey = findFish(graph, deepcopy(visited), [ex, ey])
    cnt += 1
    total += cost
print(total)
    
        
            