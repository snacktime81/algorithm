import sys

input = sys.stdin.readline


def move_block(block, board):
    if(len(block) == 2):  # 1 X 1
        x = block[0]
        y = block[1]

        while True:  # ->
            y += 1
            if(y >= 10):
                board[x][y-1] = 1
                break
            elif(board[x][y] == 1):
                board[x][y-1] = 1
                break

        y = block[1]
        while True:  # down
            x += 1
            if(x >= 10 or board[x][y] == 1):
                board[x-1][y] = 1
                break
    else:  # 2 X 1, 1 X 2
        x1, y1 = block[0], block[1]
        x2, y2 = block[2], block[3]
        while True:  # ->
            y1 += 1
            y2 += 1

            if(y1 >= 10 or y2 >= 10 or board[x1][y1] == 1 or board[x2][y2] == 1):
                board[x1][y1-1] = 1
                board[x2][y2-1] = 1
                break

        y1, y2 = block[1], block[3]

        while True:  # down
            x1 += 1
            x2 += 1
            if(x1 >= 10 or x2 >= 10 or board[x1][y1] == 1 or board[x2][y2] == 1):
                board[x1-1][y1] = 1
                board[x2-1][y2] = 1
                break


def score(board):
    result = 0
    delete = []

    for y in range(6, 10):
        tmp = 0
        for i in range(4):
            tmp += board[i][y]
        if(tmp == 4):
            for x in range(4):
                board[x][y] = 0
            result += 1
            delete.append(y)
    for d in delete:
        for y in range(d, 3, -1):
            for x in range(4):
                board[x][y] = board[x][y-1]

    delete = []

    for x in range(6, 10):
        if(sum(board[x][0:4]) == 4):
            for y in range(4):
                board[x][y] = 0
            result += 1
            delete.append(x)
    for d in delete:
        for x in range(d, 3, -1):
            for y in range(4):
                board[x][y] = board[x-1][y]
    return result


def over_line(board):
    line = 0
    tmp = 0
    tmp2 = 0
    for i in range(4):
        tmp += board[i][4]
        tmp2 += board[i][5]
    if(tmp != 0):
        line = 2
    elif(tmp2 != 0):
        line = 1

    for _ in range(line):
        for y in range(9, 3, -1):
            for x in range(4):
                board[x][y] = board[x][y-1]
    line = 0
    tmp = 0
    tmp2 = 0
    for i in range(4):
        tmp += board[4][i]
        tmp2 += board[5][i]
    if(tmp != 0):
        line = 2
    elif(tmp2 != 0):
        line = 1
    for _ in range(line):
        for x in range(9, 3, -1):
            for y in range(4):
                board[x][y] = board[x-1][y]

    for x in range(4, 6):
        for y in range(0, 4):
            board[x][y] = 0
            board[y][x] = 0


N = int(input())
board = [[0] * (10) for _ in range(10)]

result = 0

for _ in range(N):
    t, x, y = map(int, input().split())
    block = [x, y]
    if(t == 2):
        block.append(x)
        block.append(y+1)
    elif(t == 3):
        block.append(x+1)
        block.append(y)
    move_block(block, board)
    result += score(board)
    over_line(board)
    #for i in board:
    #    print(i)
    #print()
count = 0
for i in board:
    count += sum(i)
    #print(i)
print(result)
print(count)