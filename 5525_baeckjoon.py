n = int(input())
m = int(input())
OI = list(input())

p = (['I', 'O'] * (n + 1))
p.pop()

check = [False] * len(OI)

r = 0
cnt = 0
i = 0
while i < (m-2):
    print(i)
    if(OI[i] == 'I'):
        if(OI[i:i+3] == ['I', 'O', 'I']):
            cnt += 1
        else:
            cnt = 0
        if(cnt == n):
            r += 1
            cnt -= 1
    else:
        cnt = 0
    if(cnt != 0):
        i += 2
    else:
        i += 1

print(r)