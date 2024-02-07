import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

dp = [[0, 0, 0] for _ in range(N+1)]  # 우수자, 우수자x, 우수자x일때 우수자 마을과 인접 할 경우 1 아닐 경우 0
target = 1

graph = [[] for _ in range(N+1)]
people = [0] + list(map(int, input().split()))

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)


def find(node, visited):  # dp[i][0] = 
    
    visited[node] = True
    dp[node][0] = people[node]

    for n in graph[node]:
        if not visited[n]:
            find(n, visited)
            dp[node][0] += dp[n][1]
            if(dp[n][0] > dp[n][1]):
                dp[node][1] += dp[n][0]
                dp[n][2] = 1
                dp[node][2] = 1
            else:
                if(dp[n][2]):  # dp[n][1]이 우수마을과 인접하지 않음
                    dp[node][1] += dp[n][1]
                    dp[n][2] = 1
    #print(node, dp[node])

find(target, visited)

print(max(dp[target]))