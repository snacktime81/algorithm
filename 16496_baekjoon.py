import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

answer = ''
arr = []
arr2 = [ [[],[],[], []] for _ in range(10) ]
for num in numbers:
    snum = str(num)*3
    arr.append(snum)
arr.sort(reverse=True)
for i in arr:
    num = i[:len(i)//3]
    answer += num
if(int(answer) == 0):
    answer = 0
print(int(answer))