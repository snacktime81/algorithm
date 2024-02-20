import sys

sys.setrecursionlimit(10 ** 6)


def solution(tickets):
    answer = []
    ways = {}

    FULL_CNT = len(tickets)  # 사용해야하는 티켓 수

    for start, end in tickets:
        try:
            ways[start].append(end)
        except:
            ways[start] = [end]

        try:
            ways[end]
        except:
            ways[end] = []

    visited = {}
    for node in ways:
        ways[node].sort()
        visited[node] = [False] * len(ways[node])

    def dfs(node, route, ways, visited, cnt):
        # print(node, route, cnt)

        if cnt == FULL_CNT:
            return route

        for i in range(len(ways[node])):

            next_node = ways[node][i]
            # print('n', next_node)

            if not visited[node][i]:
                visited[node][i] = True
                route.append(next_node)

                r = dfs(next_node, route, ways, visited, cnt + 1)
                if r:
                    return r
                route.pop()
                visited[node][i] = False

    # print(ways)
    answer = dfs('ICN', ['ICN'], ways, visited, 0)

    return answer