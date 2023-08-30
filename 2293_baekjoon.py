import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [0] * 10001

arrCoin = []
arr[0] = 1
for i in range(n):
    coin = int(input())
    arrCoin.append(coin)

for i in arrCoin:
    for j in range(i, k+1):
        arr[j] += arr[j-i]
        
print(arr[k])

# 1 2 
