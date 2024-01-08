import sys

input = sys.stdin.readline

n = int(input())
arr = []
length = 0

for _ in range(n):
    string = input().strip()
    
    length = max(len(string), length)
    arr.append(string)
    
sum_values = dict()
values = dict()

for i in range(ord('A'), ord('Z')+1):
    sum_values[chr(i)] = 0
    values[chr(i)] = 0
    
for string in arr:
    for i in range(len(string)):
        alpha = string[i]
        sum_values[alpha] += 10**(len(string)-i-1)
        
r = 0
for i in range(9, -1, -1):
    m = 0
    
    for j in sum_values:
        m = max(m, sum_values[j])
    for j in sum_values:
        if(sum_values[j] == m):
            r += sum_values[j] * i
            sum_values[j] = 0
            break
print(r)