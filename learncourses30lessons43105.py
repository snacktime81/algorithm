def solution(tri):
    answer = 0
    move = [(1, 0), (1, 1)]

    dp = [[0] * len(tri[-1]) for _ in range(len(tri))]
    dp[0][0] = tri[0][0]
    length = 1
    for x in range(len(tri) - 1):
        for y in range(length):
            num = dp[x][y]
            dp[x + 1][y] = max(dp[x + 1][y], dp[x][y] + tri[x + 1][y])
            dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y] + tri[x + 1][y + 1])
        length += 1
    answer = max(dp[-1])
    return answer