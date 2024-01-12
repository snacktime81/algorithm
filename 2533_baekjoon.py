import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (N+1)
dp = [[0,0] for _ in range(N+1)] #  dp[node][0] = early , dp[node][1] = common

def dfs(node):
    visited[node] = True
    dp[node][0] = 1
    
    for child in graph[node]:
        if not visited[child]:
            dfs(child) # leaf에 도달하면 다음줄 실행
            dp[node][0] += min(dp[child])
            dp[node][1] += dp[child][0]

dfs(1)
r = min(dp[1])
print(r)