#https://school.programmers.co.kr/learn/courses/30/lessons/60057

s=input()
m = [0 for i in range(len(s)+1)]
m[0] = int(1e9)

for i in range(1, len(s) + 1):
        arr = []
        for j in range(0, len(s), i):
            arr.append(s[j:j+i])
        print(arr)
        index = 0
        
        repeat = arr[index]
        cnt = 1
        
        for k in range(1, len(arr)):
            index += 1
            if(arr[k] == repeat):
                cnt += 1
            
            else:
                repeat = arr[k]
                if(cnt > 1):
                    m[i] += (len(str(cnt))+i)
                else:
                    m[i] += i
                cnt = 1
        if(cnt > 1):
            m[i] += (len(str(cnt))+i)
        else:
            m[i] += len(arr[-1])
print(m)
print(min(m))
10a 10 b