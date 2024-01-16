import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    if(a > b):  #  정렬 했을때 다음 값이 무조건 앞으값으 x값 보다 작게 만들면 y 값만 신경쓰면 된다.
        arr.append([a, b])
    else:
        arr.append([b, a])

arr.sort(reverse=True, key=lambda x : (x[0], x[1]))

dp = [1] * N
for i in range(1, N):
    now_x, now_y = arr[i]
    
    for j in range(i):
        pre_x, pre_y = arr[j]
        if(now_y <= pre_y): # now_x는 무조건 pre_x보다 크다
            dp[i] = max(dp[i], dp[j] + 1)
#print(arr)
#print(dp)
print(max(dp))
