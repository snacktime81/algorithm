import sys
input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        if(i == j):
            dp[i][j] = 1
        elif(j-i == 1 and arr[j] == arr[i]): # 연속된 두수
            dp[i][j] = 1
        else: # i != j
            if(arr[i] == arr[j] and dp[i+1][j-1]):
                dp[i][j] = 1
            else:
                dp[i][j] = 0

questions = int(input())

for _ in range(questions):
    x, y = map(int, input().split())
    print(dp[x][y])