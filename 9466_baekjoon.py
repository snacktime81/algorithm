import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, c, l, start):
    next_i = choices[i-1]
    c[i] = 1
    l.append(i)
    
    if(next_i == start):
        for k in l:
            team[k] = True
        return True
    
    if(team[next_i] == True):
        for k in l:
            team[k] = -1
        return False
    
    if(team[next_i] == -1):
        for k in l:
            team[k] = -1
        return False
    

    check = False
    
    if(c[next_i] == 1):
        for k in l:
            if( k == next_i):
                check = True
                team[k] = True
            elif(check):
                team[k] = True
            else:
                team[k] = -1
        return False
    

    return dfs(next_i, c, l, start)


T = int(input())

for _ in range(T):
    n = int(input())
    choices = list(map(int, input().split()))
    
    r = 0
    team = [False for i in range(n+1)]
    c = [0] * (n+1)
    
    for i in range(1, n+1):
        if(team[i] == True):
            continue
        if(team[i] == -1):
            r += 1
            continue
            
        k = dfs(i,c, [], i)
        if(k):
            continue
        else:
            r += 1
    print(r)