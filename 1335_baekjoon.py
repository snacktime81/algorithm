import sys

n, w, l = map(int, sys.stdin.readline().split())


trucks = list(map(int, sys.stdin.readline().split()))

cnt = 0
sl = 0

bridges = [0] * w
while(len(bridges) != 0):
    bridges.pop(0)
    cnt += 1
    if len(trucks) != 0:

        if(sum(bridges) + trucks[0] <= l):
            t = trucks.pop(0)
            bridges.append(t)
        else:
            bridges.append(0)

print(cnt)
