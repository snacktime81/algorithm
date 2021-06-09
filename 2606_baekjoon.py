# 2606
import sys

c = int(sys.stdin.readline())
n = int(sys.stdin.readline())
nod = []
dic = {}

for i in range(c):
    dic[i+1] = set()
for j in range(n):
  a, b = map(int, sys.stdin.readline().split())
  dic[a].add(b) #dic[a]가 set이라 .add가 가능
  dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)
