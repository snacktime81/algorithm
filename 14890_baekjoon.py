import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = []

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

cnt = 0

for line in graph:
    check = True
    way = [False] * n
    for i in range(n-1):
        
        nowValue = line[i]
        nextValue = line[i+1]
        if(abs(nextValue-nowValue) > 1):
            check = False
            break
        
        elif(nextValue-nowValue == 1):
            for j in range(l):
                index = i - j
                if(index<0 or line[index] != nowValue or way[index]):
                    check = False
                    break
                else:
                    way[index] = True
        elif(nowValue-nextValue == 1):
            for j in range(1, l+1):
                index = i + j
                if(index >= n or line[index] != nextValue or way[index]):
                    check =False
                    break
                else:
                    way[index] = True
        #print( way)
    if(check):
        #print(line)

        cnt += 1


for i in range(n):
    check = True
    way = [False] * n
    for j in range(n-1):

        nowValue = graph[j][i]
        nextValue = graph[j+1][i]
        if(abs(nextValue-nowValue) > 1):
            check =False
            break
        elif(nextValue-nowValue == 1):
            for k in range(l):
                index = j - k
                if(index < 0 or graph[index][i] != nowValue or way[index]):
                    check = False
                    break
                else:
                    way[index] = True

        elif(nowValue-nextValue == 1):
            for k in range(1, l+1):
                index = j + k
                if(index >= n or graph[index][i] != nextValue or way[index]):
                    check = False
                    break
                else:
                    way[index] = True
        #print(i, way)
                
    if(check):
        #print(i)
        cnt += 1


print(cnt)
                    