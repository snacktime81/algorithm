import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def turn(arr, k, direction):
    if(direction == 1):
        for _ in range(k):
            tmp = arr.popleft()
            arr.append(tmp)
    else:
        for _ in range(k):
            tmp = arr.pop()
            arr.appendleft(tmp)
    return 0


def remove_near_value(arrs):
    check = False
    tmp = deepcopy(arrs)

    for x in range(len(arrs)):
        for y in range(len(arrs[x])):
            value = arrs[x][y]
            if(value == 0):
                continue
            up = x + 1 if (x+1) < n else -1
            down = x - 1 if (x-1) >= 0 else -1
            left = y - 1 if (y-1) >= 0 else len(arrs[x])-1
            right = y + 1 if (y+1) < len(arrs[x]) else 0

            if(up != -1):
                if(value == arrs[up][y]):
                    check = True
                    tmp[up][y] = 0
                    tmp[x][y] = 0
            if(down != -1):
                if(value == arrs[down][y]):
                    check = True
                    tmp[down][y] = 0
                    tmp[x][y] = 0
            if(value == arrs[x][left]):
                check = True
                tmp[x][left] = 0
                tmp[x][y] = 0
            if(value == arrs[x][right]):
                check = True
                tmp[x][right] = 0
                tmp[x][y] = 0
    return check, tmp


def change_avg(arrs):
    r = 0
    cnt = 0
    for arr in arrs:
        for num in arr:
            if(num != 0):
                r += num
                cnt += 1
    if(cnt == 0):
        return True
    avg = r / cnt

    for x in range(len(arrs)):
        for y in range(len(arrs[x])):
            if(arrs[x][y] != 0):
                if(arrs[x][y] < avg):
                    arrs[x][y] += 1
                elif(arrs[x][y] > avg):
                    arrs[x][y] -= 1
    return False 

n, m, t = map(int, input().split())

circles = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    q = deque(numbers)
    circles.append(q)

for _ in range(t):
    x, d, k = map(int, input().split())
    original_x = x
    count = 2
    
    while x <= n:
        turn(circles[x-1], k, d)
        x = original_x * count
        count += 1
        
    # for i in circles:
    #     print(i)
    # print()
    check, circles = remove_near_value(circles)
    
    
    check2 = False
    if(not check):
        check2 = change_avg(circles)
    if(check2):
        break

r = 0

for circle in circles:
    for i in circle:
        r += i
print(r)
