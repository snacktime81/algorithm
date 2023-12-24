#

import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    high = []
    low =[]
    
    check = dict()
    
    l = 0
    n = int(input())

    for i in range(n):
        command, num = input().strip().split()
        num = int(num)
        if(command == 'I'):
            heapq.heappush(low, num)
            heapq.heappush(high, -num)
            try:
                if(check[num] >= 0):
                    check[num] += 1
            except:
                check[num] = 1
            l += 1
        else:
            if(l > 0):
                if(num == -1):
                    while True:
                        k = heapq.heappop(low)
                        if(check[k] > 0):
                            check[k] -= 1
                            break
                else:
                    while True:
                        k = -heapq.heappop(high)
                        if(check[k] > 0):
                            check[k] -= 1
                            break
                    
                l -= 1
    tmp  = []
    result= []
    if(l == 0):
        print('EMPTY')
    elif(l == 1):
        while True:
            n = heapq.heappop(low)
            if(check[n] > 0):
                check[n] -= 1
                break
        print(n, n)
    else:
        while True:
            min_n = heapq.heappop(low)
            if(check[min_n] > 0):
                check[min_n] -= 1
                break
        while True:
            max_n = -heapq.heappop(high)
            if(check[max_n] > 0):
                break
        print(max_n, min_n)