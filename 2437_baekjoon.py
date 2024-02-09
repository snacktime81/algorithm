N = int(input())
weights = list(map(int, input().split()))

weights.sort()

dp = set()
max_num = weights[0]
r = 1

if(max_num > 1):
    print(1)
else:
    c = True
    for i in range(1, N):
        num = weights[i]

        if(num <= max_num+1):
            max_num = num + max_num
        else:
            print(max_num+1)
            c = False
            break
    if(c):
        print(max_num+1)
