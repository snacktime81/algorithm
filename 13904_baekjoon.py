import sys
N = int(input())

homeworks = []
time = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    homeworks.append(arr)
    time = max(time, arr[0])
    
homeworks.sort(reverse=True, key=lambda x:x[1])
dp =  [0] * (time)

check = [False] * (time+1)
print(homeworks)
for time, score in homeworks:
    if(not check[time]):
        check[time] = score
    else:
        while time>0:
            if(not check[time]):
                check[time] = score
                break
            time -= 1
print(sum(check))