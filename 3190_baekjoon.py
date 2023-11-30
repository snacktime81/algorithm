import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

apples = []

move = [(0,1), (1,0),(0,-1),(-1,0)] # 오른쪽으로 회전시 index도 1증가 왼쪽을 회전은 -1

for _ in range(k):
    x, y = map(int, input().split())
    apples.append([x-1, y-1])

l = int(input())

snake = [[0,0]]

def movef(snake, d):
    h_x, h_y = snake[0]
    dx = h_x + move[d][0]
    dy = h_y + move[d][1]
    #print(h_x, h_y)
    #print(dx, dy)
    
    if( dx < 0 or dy < 0 or dx >= n or dy >= n):
        return True
    
    if([dx, dy] in snake):
        return True
    
    snake[0] = [dx, dy]
    

    for i in range(1, len(snake)):
        tmp_x, tmp_y = snake[i]
        snake[i] = [h_x, h_y]
        h_x, h_y = tmp_x, tmp_y
    if([dx, dy] in apples):
        snake.append([h_x, h_y])
        apples.remove([dx, dy])
    
    #print(snake)
        
turn = {}
d = 0
check = False
cnt = 0
for _ in range(l):
    x, c = input().rstrip().split()
    turn[int(x)] = c
for i in range(1, 10001):
    if(i in turn):
        check = movef(snake,d)
        if(turn[i] == 'D'):
            d = (d+1)%4
        else:
            if(d-1<0):
                d=3
            else:
                d -= 1
        #print(i, d)
    else:
        check = movef(snake,d)

    if(check):
        print(i)
        break