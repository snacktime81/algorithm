#2579
import sys
input = sys.stdin.readline

n = int(input())

arrS = [0] * (n+1)
arr = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(input())
    

arrS[1] = arr[1]

if(n >= 2):
    arrS[2] = arr[2] + arr[1]
if(n >= 3):
    for i in range(3, n+1):
        arrS[i] = max( (arrS[i-2] + arr[i]), (arrS[i-3] + arr[i-1] + arr[i]) )


print(arrS[n])


    