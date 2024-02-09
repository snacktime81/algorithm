INF = int(1e9)

N, M = map(int, input().split())

books = list(map(int, input().split()))

if(max(books) > abs(min(books))):
    books.sort()
else:
    books.sort(reverse=True)

books = [0] + books
    
dp = [[0] * (M+1) for _ in range(N+1)] # dp[현재 가져다 놓을 책의 번호][원점에서 가져간 책의 수]
for i in range(N+1):
    dp[i][0] = INF

for i in range(1, N+1):
    dp[i][1] = min(dp[i-1]) + abs(books[i-1]) + abs(books[i])  # dp[i][1]은 원점에서 지금 가져다 놓을 책 1권만 가져놓을 경우 임으로 min(dp[i-1]에서 books[i-1]이 원점으로 돌아가는 비용이고, 원점에서 현재 책을 가져다 놓는 비용인 books[i]값을 더해준다.
    
    for j in range(2, M+1):
        if(j > i):
            dp[i][j] = INF
        else:
            dp[i][j] = dp[i-1][j-1] + abs(books[i-1] - books[i])  # 2권 이상의 책을 가져올 경우에는 원점을 방문할 필요가 없이 현재 위치인 books[i-1]에서 가져다 놓을 책의 위치인 books[i]까지의 거리만 더해주면 된다.
print(min(dp[-1]))