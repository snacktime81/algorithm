import sys

n = int(sys.stdin.readline())

gift = []
for i in range(n):
    t = list(map(int, (sys.stdin.readline().split())))
    if(len(t) == 1 and len(gift) == 0):
        print(-1)
    elif(len(t) == 1 and len(gift) != 0):
        print(gift.pop(0))
    else:
        for l in range(1, t[0]+1):
            gift.append(t[l])
        gift = sorted(gift, reverse=True)