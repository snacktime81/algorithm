# https://www.acmicpc.net/problem/14891
import sys
from collections import deque

input = sys.stdin.readline

class wheel:
    def __init__(self,a,b,c,d,e,f,g,h):
        
        self.tooth = deque([])
        self.tooth.append(a)
        self.tooth.append(b)
        self.tooth.append(c)
        self.tooth.append(d)
        self.tooth.append(e)
        self.tooth.append(f)
        self.tooth.append(g)
        self.tooth.append(h)
        
    def turn(self, f):
        if( f == -1):
            tmp = self.tooth.popleft()
            self.tooth.append(tmp)
        else:
            tmp = self.tooth.pop()
            self.tooth.appendleft(tmp)
            
    def find(self, i):
        return self.tooth[i-1]
    
wheels = []

for _ in range(4):
    line = list(input().rstrip())
    nums = []
    for i in line:
        nums.append(int(i))
    a,b,c,d,e,f,g,h = nums
    wheels.append(wheel(a,b,c,d,e,f,g,h))
    
k = int(input())
re = {1:-1, -1:1}
for i in range(k):
    w, f = map(int, input().split())
    a = wheels[0].find(3)
    A = wheels[1].find(7)
    b = wheels[1].find(3)
    B = wheels[2].find(7)
    c = wheels[2].find(3)
    C = wheels[3].find(7)
    
    if(w==1):
        if(a != A):
            if(b != B):
                if(c != C):
                    for i in range(4):
                        wheels[i].turn(f)
                        f = re[f]
                else:
                    for i in range(3):
                        wheels[i].turn(f)
                        f = re[f]
            else:
                for i in range(2):
                    wheels[i].turn(f)
                    f = re[f]
        else:
            wheels[0].turn(f)
            f = re[f]
    
    elif(w == 2):
        if( a != A and b != B):
            if(c != C):
                wheels[1].turn(f)
                f = re[f]
                wheels[0].turn(f)
                wheels[2].turn(f)
                f=re[f]
                wheels[3].turn(f)
            else:
                wheels[1].turn(f)
                f = re[f]
                wheels[0].turn(f)
                wheels[2].turn(f)
        elif(a != A and b == B):
            wheels[1].turn(f)
            f = re[f]
            wheels[0].turn(f)
            f=re[f]
        elif(a == A and b != B):
            if(c != C):
                wheels[1].turn(f)
                f = re[f]
                wheels[2].turn(f)
                f=re[f]
                wheels[3].turn(f)
                f= re[f]
            else:
                wheels[1].turn(f)
                f = re[f]
                wheels[2].turn(f)
                f=re[f]
        elif(a == A and b == B):
            wheels[1].turn(f)
            f = re[f]
    elif(w==3):
        if( c != C and b != B):
            if(a != A):
                wheels[2].turn(f)
                f = re[f]
                wheels[1].turn(f)
                wheels[3].turn(f)
                f=re[f]
                wheels[0].turn(f)
            else:
                wheels[2].turn(f)
                f = re[f]
                wheels[1].turn(f)
                wheels[3].turn(f)
        elif(c != C and b == B):
            wheels[2].turn(f)
            f = re[f]
            wheels[3].turn(f)
            f=re[f]
        elif(c == C and b != B):
            if(a != A):
                wheels[2].turn(f)
                f = re[f]
                wheels[1].turn(f)
                f=re[f]
                wheels[0].turn(f)
                f= re[f]
            else:
                wheels[2].turn(f)
                f = re[f]
                wheels[1].turn(f)
                f=re[f]
        else:
            wheels[2].turn(f)
            f = re[f]
    else:
        if(c != C):
            if(b != B):
                if(a != A):
                    for i in range(3, -1, -1):
                        wheels[i].turn(f)
                        f = re[f]
                else:
                    for i in range(3, 0, -1):
                        wheels[i].turn(f)
                        f = re[f]
            else:
                for i in range(3, 1, -1):
                    wheels[i].turn(f)
                    f = re[f]
        else:
            wheels[3].turn(f)
            f = re[f]
    # for i in wheels:
    #     print(i.tooth)
result = 0
for i in range(4):
    score = 0 if wheels[i].find(1) == 0 else 2**(i)
    result += score
print(result)
