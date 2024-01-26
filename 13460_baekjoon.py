import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
graph = []
balls = [[0, 0], [0, 0]]  # red blue


for i in range(N):
    line = list(input().rstrip())
    graph.append(line)

    for j in range(M):
        if(line[j] == 'R'):
            balls[0][0] = i
            balls[0][1] = j
        elif(line[j] == 'B'):
            balls[1][0] = i
            balls[1][1] = j

q = deque([(balls[0][0], balls[0][1], balls[1][0], balls[1][1], 0)])
check = False
while q:
    rx, ry, bx, by, cnt = q.popleft()
    print(cnt)
    if(cnt >= 10):
        print(-1)
        break
    for i in move:
        drx, dry, dbx, dby = rx, ry, bx, by
        count = cnt + 1
        move_block_cnt = 0
        while True:
            trx = drx + i[0]
            tryy = dry + i[1]
            tbx = dbx + i[0]
            tby = dby + i[1]

            rblock = graph[trx][tryy]
            bblock = graph[tbx][tby]

            if(rblock == '#' and bblock == '#'):
                if(move_block_cnt == 0):
                    break
                q.append([drx, dry, dbx, dby, count])
                break
            if(rblock == '#'):
                trx = drx
                tryy = dry
            if(bblock == '#'):
                tbx = dbx
                tby = dby
            if(trx == tbx and tryy == tby):
                q.append([drx, dry, dbx, dby, count])
                break
            if(bblock == 'O'):
                break
            if(rblock == 'O'):
                check = True
                while  True:
                    tmpx = tbx + i[0]
                    tmpy = tby + i[1]
                    if(graph[tmpx][tmpy] == '#'):
                        break
                    elif(graph[tmpx][tmpy] == 'O'):
                        check = False
                        break
                    tbx = tmpx
                    tby = tmpy
                if(check):  
                    print(cnt + 1)
                break
            drx, dry, dbx, dby = trx, tryy, tbx, tby
            move_block_cnt += 1
        if(check):
            break
    if(check):
        break
