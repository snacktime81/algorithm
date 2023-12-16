# https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline

n = int(input())
s = [0] * (21)
for _ in range(n):
    k = input().split()
    if(k[0] == 'all'):
        s = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif(k[0] == 'empty'):
        s = [0] * 21
    else:
        c, num = k
        num = int(num)
        if(c == 'add'):
            s[num] = 1
        elif(c=='remove'):
            s[num] = 0
        elif(c=='check'):
            if(s[num] == 1):
                print(1)
            else:
                print(0)
        elif(c == 'toggle'):
            if(s[num] == 1):
                s[num] = 0
            else:
                s[num] = 1