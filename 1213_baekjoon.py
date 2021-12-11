#1213

s = input()
s = list(s)
i = 0
r = len(s) - 1
s = sorted(s)
b =True
cnt = 0
while i < r:
    if(s[i] == s[r]):
        i += 1
        r -= 1
    else:
        key = s[i]
        for j in range((i+1), r):
            if s[j] == s[i]:
                for k in range(j, r):
                    s[k] = s[k+1]
                s[r] = s[i]
                i += 1
                r -= 1
                break
        else:
            if(cnt > len(s)):
                b= False
                break
            else:
                tmp = s[i]
                for k in range((i), r):
                    s[k] = s[k+1]
                s[r] = tmp
                cnt += 1

if(b):
    print("".join(s))
else:
    print("I'm Sorry Hansoo")