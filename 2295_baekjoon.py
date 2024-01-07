import sys

n = int(input())
d = dict()

arr = []

for i in range(1, n+1):
    num = int(input())
    arr.append(num)

for i in arr:
    for j in arr:
        d[i+j] = 1

result = []

# a+b = r - c

for i in arr:
    for j in arr:
        try:
            tmp = d[i-j]
            
            k = i-j+j
            
            result.append(k)
            break
        except:
            continue
print(max(result))