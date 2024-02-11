N = int(input())


evens = []
check = [True] * (N+1)
check[0] = False
check[1] = False



for i in range(2, N+1):
    if(check[i]):
        evens.append(i)
        
        tmp = 2
        while i * tmp <= N:
            check[tmp*i] = False
            tmp += 1

# visited = [0] * (N+1)
cnt = 0
            
# for i in range(len(evens)):
#     tmp = evens[i]
#     if(tmp == N):
#         cnt += 1
        
#     for j in range(i+1, len(evens)):
#         tmp += evens[j]
#         if(tmp == N):
#             cnt += 1
#         elif(tmp > N):
#             break


c_sum = [0] * (len(evens))
tmp = 0
for i in range(len(evens)):
    tmp += evens[i]
    c_sum[i] = tmp

left = 0
right = 0

while right < len(evens):
    a = c_sum[right]
    b = 0 if left == 0 else c_sum[left-1]
    s = a - b
    if(s == N):
        cnt += 1
        left += 1
    elif(s < N):
        right += 1
    else:
        left += 1
        
print(cnt)
            