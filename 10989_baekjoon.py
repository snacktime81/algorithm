import sys

n = int(sys.stdin.readline())
li = [0] * 10001

for i in range(n):
    n = int(sys.stdin.readline())
    li[n] += 1

for i in range(10001):
    if(li[i] == 0):
        continue
    elif(li[i] == 1):
        print(i)
    else:
        for _ in range(li[i]):
            print(i)
