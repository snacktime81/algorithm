# https://www.acmicpc.net/problem/1309

n = int(input())

# dp[i] = dp[i-1] + (dp[i-2] * 2) + (dp[i-1] - dp[i-2])

one = 1
two = 3
result = 3

for i in range(2, n+1):
    result = (one + two*2) % 9901
    one = two % 9901
    two = result % 9901
print(result)