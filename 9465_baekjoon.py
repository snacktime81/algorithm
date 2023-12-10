# https://www.acmicpc.net/problem/9465
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    graph = []
    dp = []
    for _ in range(2):
        line = list(map(int,input().split()))
        graph.append(line)
        dp.append(line)
        
    if(n == 1):
        print(max(graph[0][0], graph[1][0]))
    if(n == 2):
        first = graph[0][0] + graph[1][1]
        second = graph[1][0] + graph[0][1]
        print(max(first, second))
    else:
        dp[0][1] = graph[0][1] + graph[1][0]
        dp[1][1] = graph[0][0] + graph[1][1]
        for i in range(2, n):
            dp[0][i] += max(graph[1][i-1], max(graph[0][i-2], graph[1][i-2]))
            dp[1][i] += max(graph[0][i-1], max(graph[0][i-2], graph[1][i-2]))
    print(max(dp[0][-1], dp[1][-1]))
        