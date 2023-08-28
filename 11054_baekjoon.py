n = int(input())

small = []
big = []

arr = list(map(int, input().split()))

small.append(1)
big.append(1)



for i in range(1, len(arr)):
    sNum = 1
    bNum = 1
    for j in range(len(small)):
        
        if(arr[j] < arr[i] and sNum <= small[j]):
            sNum = small[j] + 1
        
        if(arr[j] > arr[i]):
            s = small[j]
            b = big[j]
            
            num = max(s, b)
            
            if(bNum <= num):
                bNum = num + 1
    small.append(sNum)
    big.append(bNum)
#print(small, big)
num = max(max(small), max(big))
print(num)