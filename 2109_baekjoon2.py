import sys

input = sys.stdin.readline


N = int(input())

data = []
last_day = 0

for _ in range(N):
    fee, day = map(int, input().split())
    data.append([fee, day])
    last_day = max(last_day, day
                  )
data.sort(reverse=True)
costs = [0] * (last_day+1)

parent = [i for i in range(last_day+1)]

for fee, day in data:
    for i in range(day, 0, -1):
        if(costs[i] == 0):
            costs[i] = fee
            break
print(sum(costs))
