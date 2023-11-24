import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
cost = [ [0]*c for _ in range(r)]
check = []
cost[0][0] = 1

move = [(1,0), (-1,0), (0,1), (0,-1)]


def dfs(graph, x, y, cost, check, newCost):
    check.append(graph[x][y])
    newCost += 1
    for i in move:
        dx = x + i[0]
        dy = y + i[1]
        #print(cost)
        if(dx < 0 or dy < 0 or dx >= r or dy >= c):
            continue
        if(graph[dx][dy] in check):
            continue
        
        if(cost[dx][dy] < newCost):
            cost[dx][dy] = newCost
        #print('dx, dy: ', dx, ' ', dy, ' ', newCost)
        dfs(graph,dx,dy,cost,check,newCost)
        
        if(newCost == 26):
            return True
        
        check.pop()
        #print(check)
if(dfs(graph, 0, 0, cost, check, 1)):
    print(26)
else:
    maxCost = 0
    for i in cost:
        if(maxCost < max(i)):
            maxCost = max(i)
    #print('cost ', cost)
    print(maxCost)
