import sys

input = sys.stdin.readline


def find(parent, x):
    if(parent[x] != x):
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(a, b, parent):
    a = find(parent, a)
    b = find(parent, b)
    
    if( a < b):
        parent[b] = a
    else:
        parent[a] = b

case = 0


while(True):
    n, m = map(int, input().split())
    
    if(n == 0 and m == 0):
        break
    
    case += 1
    parent = [i for i in range(n+1)]
    cycle = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        #print('n,m: ', n, m)
        if(find(parent, a) == find(parent, b)):
            cycle.append(find(parent, a))
        union(a, b, parent)
        
    
    
    cnt = 0
    
    for i in range(1,n+1):
        find(parent, i)
    for i in range(len(cycle)):
        cycle[i] = find(parent, cycle[i])
        
    noTrees = []
    
    for i in range(1, n+1):
        if( i == parent[i] and i not in cycle):
            cnt += 1
    
    #print(parent)
    #print(cycle)
    
    if(cnt == 0):
        print(f"Case {case}: No trees.")
    elif(cnt == 1):
        print(f"Case {case}: There is one tree.")
    else:
        print(f'Case {case}: A forest of {cnt} trees.')