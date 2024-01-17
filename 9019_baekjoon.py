import sys
from collections import deque

input = sys.stdin.readline
command_alpha = {0:'D', 1:'S', 2:'L', 3:'R'}
T = int(input())


def command(order, num):

    if(order == 0): #  D   
        num = num*2 % 10000
        return num
    elif(order == 1): #  S
        if(num == 0):
            num = 9999
        else:
            num -= 1
        return num
    elif(order == 2): #  L
        front = num // 1000
        back = num % 1000
        num = back * 10 + front
        return num
    elif(order == 3): #  R 0231 1023
        front = num // 10
        back = num % 10
        num = back*1000 + front
        return num
    else:
        return 0


for _ in range(T):

    visited = [False] * (10000)

    A, B = map(int, input().split())

    q = deque()
    q.append([A, ''])
    visited[A] = True
    r = 0
    while q:
        num, commands = q.popleft()
        if(num == B):
            r = commands
            break
        for i in range(4):
            d_num = command(i, num)
            if not visited[d_num]:
                d_commands = commands + command_alpha[i]
                q.append([d_num, d_commands])
                visited[d_num] = True
    print(r)