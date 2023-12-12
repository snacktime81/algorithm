s = input()

r1 = 0
r2 = 0

check = bool(int(s[0]))

for i in s:
    if(int(i) == 1):
        if(check == True):
            r1 += 1
            check = False
    if(int(i) == 0):
        if(check == False):
            r2 += 1
            check = True
    
print(min(r1, r2))