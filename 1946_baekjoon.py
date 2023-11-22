# 1946
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    n = int(input())
    
    users = [] # 모든 지원자
    usersRe= [] # 합격하는 지원자
    
    for i in range(n): # 모든 지원자 입력 받기
        
        user = list(map(int, input().split()))
        
        users.append(user)
    
    users.sort(reverse=True) # 역순으로 정렬 역순인 이유는 pop을 이용하여 삭제를 빠르게 하기 위함
    
    l = n - 1 # 남은 모든 지원자의 수 - 1 = users의 index
    
    dx, dy = users[l] # do
    usersRe.append([dx,dy])
    users.pop()
    l -= 1
    minY = dy
    
    while users: # while
        dx, dy = users[l]
        

        for x, y in usersRe:
            if(dy > y):
                break
            elif(dy < minY):
                minY = dy
                usersRe.append([dx, dy])
                break
            
        users.pop()
        l -= 1
    
    #print('re: ', usersRe)
    print(len(usersRe))
      
