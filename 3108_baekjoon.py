import sys
input = sys.stdin.readline

def find(x):
    if(parent[x] != x):
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if(a<b):
        parent[b] = a
    else:
        parent[a] = b


r = 0
x = [[] for _ in range(1001)] # * (1001) # -500 ~ 500
y = [[] for _ in range(1001)] #* (1001)
n = int(input())

parent = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500
    x2 += 500
    y1 += 500
    y2 += 500
    graph[i].append([x1,x2])
    graph[i].append([y1,y2])
    if((x1 == 500 and y1 ==500) or( x2 == 500 and y2 == 500)):
        r = -1
    elif((x1 == 500 or x2 == 500) and y1 <= 500 <= y2):
        r = -1
    elif((y1 == 500 or y2 == 500) and x1 <= 500 <= x2):
        r = -1
    s = set()
    
    
    for j in range(x1, x2+1):
        for k in x[j]:
            if((graph[k][1][0] <= y1 <= graph[k][1][1]) or (graph[k][1][0] <= y2 <= graph[k][1][1])):
                s.add(k)
    for j in range(y1, y2+1):
        for k in y[j]:
            if((graph[k][0][0] <= x1 <= graph[k][0][1]) or (graph[k][0][0] <= x2 <= graph[k][0][1])):
                s.add(k)
    for j in s:
        union(i, j)
        
    x[x1].append(i)
    x[x2].append(i)
    y[y1].append(i)
    y[y2].append(i)
    
for i in range(1, n+1):
    parent[i] = find(i)
#print(parent)
for i in range(1, n+1):
    if(i == parent[i]):
        r += 1
        
print(r)