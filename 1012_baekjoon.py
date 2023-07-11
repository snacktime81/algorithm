import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

move = [(0,1), (0, -1), (1, 0), (-1, 0)]


T = int(input())

for _ in range(T):

    m, n, k = map(int, input().split())

    maps = []
    visited = []

    for _ in range(n):
        maps.append([0] * m)
        visited.append([False] * m)
    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1

    def dfs(maps, x, y):

        if(maps[x][y] == 1):

            maps[x][y] = 0

            for i in move:

                dx = x + i[0]
                dy = y + i[1]

                if(dx < 0 or dx >= n or dy < 0 or dy >= m):
                    continue

                dfs(maps, dx, dy)
            return True
        return False


    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(maps, i,j):
                result += 1


    print(result)