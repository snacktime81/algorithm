N = int(input())
NUMS = list(map(int, input().split()))
NUMS.sort()
r = int(1e11)
arr = []
for i in range(N-1):
    num = NUMS[i]
    left = i+1
    right = N-1
    while left < right:
        value = num + NUMS[left] + NUMS[right]
        if(abs(r) > abs(value)):
            r = value
            arr = [NUMS[i],NUMS[left],NUMS[right]]
            
        if(value == 0):
            arr =[NUMS[i],NUMS[left],NUMS[right]]
            r = 0
            break
        elif(value < 0):
            left += 1

        else:
            right -= 1
            
for i in arr:
    print(i, end=' ')
