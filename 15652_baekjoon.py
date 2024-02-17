N, M = map(int, input().split())

arr = []

def dfs(num, result):
    result += str(num) + ' '
    #print(num)
    if len(result) == M * 2:
        arr.append(result.rstrip())
        return 0
    for i in range(num, N+1):
            dfs(i, result)

for i in range(1, N+1):
    dfs(i, '')
for i in arr:
    print(i)