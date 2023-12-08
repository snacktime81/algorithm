#https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if(computers[i][j] == 1):
                union(i, j, parent)
    
    result = [ False] * n
    
    for i in range(n):
        find(i, parent)
    
    for i in parent:
        result[i] = True
    for i in result:
        if(i):
            answer += 1
    return answer

def find(x, parent):
    if(parent[x] != x):
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a,b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if(a < b):
        parent[b] = a
    else:
         parent[a] = b