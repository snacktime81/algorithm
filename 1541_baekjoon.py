#1541
import sys
input = sys.stdin.readline

math = ['+', '-']

sik = list(input().rstrip())

arr = []

num =''

for i in range(len(sik)):
    if(sik[i] in math):
        arr.append(str(int(num)))
        arr.append(sik[i])
        num = ''
    else:
        num += sik[i]
    if(i == len(sik)-1):
        arr.append(str(int(num)))

#print(arr)

e = "".join(arr).split('-')


for i in range(len(e)):
    e[i] = eval(e[i])

result = e[0]

for i in range(1, len(e)):
    result -= e[i]
print(result)