n, m = map(int, input().split())
coinArr = []
arr = [0] * (10001)

for i in range(n):
    coin = int(input())
    coinArr.append(coin)
    arr[coin] = 1
    
for i in range(1, m+1):
    
    if(arr[i] == 1):
        continue
    
    tmp = []
    
    for j in coinArr:
        if(j >= i):
            break
        
        if(arr[i-j] == 0):
            continue
        
        else:
            tmp.append(arr[i-j] + 1)
        
    if(tmp):
        arr[i] = min(tmp)
    else:
        arr[i] = 0
        
if arr[m] == 0:
    print(-1)
else:
    print(arr[m])
    
