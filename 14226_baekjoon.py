from heapq import heappush, heappop

N = int(input())

dp = [[1e9] * (10000) for _ in range(10000)]  # dp[숫자][클립보드]

q = []
heappush(q, (0, 1, 0))

dp[1][0] = 0
while q:
    try:
        time, num, clip = heappop(q)
            
        if(dp[num + clip][clip] > time + 1):
            heappush(q, (time+1, num + clip, clip))
            dp[num+clip][clip] = time+1

        if(dp[num][num] > time+1):
            heappush(q, (time+1, num, num))
            dp[num][num] = time+1
        if(num-1 > 0 and dp[num-1][clip] > time+1):
            heappush(q, (time+1, num-1, clip))
            dp[num-1][clip] = time+1
    except:
        break

print(min(dp[N]))

