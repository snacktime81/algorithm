import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    command = list(input().rstrip())
    n = int(input())
    x = input().rstrip()
    x = x[1:-1]
    if(len(x) == 0):
         q = deque()
    else:
        x = list(x.split(','))
        q= deque()
        for i in x:
            q.append(i)

    check = True
    r = False
    for c in command:
        if c == "R":
            r = not r
        if c == "D":
            if(len(q) == 0):
                print('error')
                check = False
                break
            else:
                if(not r):
                    q.popleft()
                else:
                    q.pop()
    if(not check):
        continue
    if(r):
        print('[', end='')
        while q:
            num = q.pop()
            print(num, end='')
            if(len(q) >= 1):
                print(',', end='')
        print(']')
    else:
        print('[', end='')
        while q:
            num = q.popleft()
            print(num, end='')
            if(len(q) >= 1):
                print(',', end='')
        print(']')