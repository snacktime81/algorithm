n = int(input())

length = list(map(int, input().split()))
cost = list(map(int ,input().split()))

m = min(cost)
result = 0
k = cost[0]
for i in range(n-1):
    if(i == 0):
        result += length[i] * k
        continue
    if(cost[i] > k):
        result += length[i] * k
    else:
        k = cost[i]
        result += length[i] * k
print(result)