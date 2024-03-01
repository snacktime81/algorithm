N = int(input())

nums = []

for _ in range(N):
    num = int(input())
    nums.append(num)

q = []
index = 0
num = 1
result = []
while index < N:

    if num > N+1:
        result = False
        break

    if not q:
        q.append(num)
        result.append('+')
        num += 1
    elif q[-1] == nums[index]:
        q.pop()
        result.append('-')
        index += 1
    else:
        q.append(num)
        result.append('+')
        num += 1

if not result:
    print('NO')
else:
    for i in result:
        print(i)