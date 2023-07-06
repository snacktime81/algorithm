from collections import deque

def bfs(map):
    n = len(map)
    m = len(map[0])
    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, -1, 1]

    queue = deque([(0, 0)])
    while(queue):
        x, y = queue.popleft()
        for i in range(len(moveX)):
            dx = x + moveX[i]
            dy = y + moveY[i]

            if(dx < 0 or dx >= n or dy < 0 or dy >= m):
                continue

            if(map[dx][dy] != 1):
                continue
            if(map[dx][dy] == 1):
                queue.append((dx, dy))
                map[dx][dy] = map[x][y] + 1

    return map
    

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    cost = bfs(maps)
    if(cost[n-1][m-1] != 1):
        answer = cost[n-1][m-1]
    else:
        answer = -1
    print(answer)
    return answer