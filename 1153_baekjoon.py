N = int(input())

evens = [True] * (N+1)
data = []

for i in range(2, N+1):
    if(evens[i]):
        key = 2
        while i * key < N+1:
            evens[key*i] = False
            key += 1
        data.append(i)
        
if( N < 8):
    print(-1)
else:
    num = N - 4 if N % 2 == 0 else N - 5
    result = [2, 2] if N % 2 == 0 else [2, 3]
    check = False
    for i in data:
        for j in data:
            if(i+j == num):
                result.append(i)
                result.append(j)
                check = True
                break
            elif(i+j > num):
                break
        if(check):
            break
            
    for i in result:
        print(i, end=' ')


    