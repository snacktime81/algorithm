import math
# 웅덩이가 좌표가 아니라 1~2 사이에 웅덩이가 있다는 형식의 공간
N, L = map(int, input().split())

arrs = []
for _ in range(N):
    s, e = map(int, input().split())
    arrs.append([s, e])

arrs.sort()
last_step = -1
cnt = 0

for s, e in arrs:
    if(s < last_step):
        s = last_step

    #웅덩이 수 = e - s
    
    #놓을 수 있는 판자 수 x = math.ceil((e - s) / L )
    
    #판자가 마지막으로 놓인 위치 s + x * L
    x = math.ceil((e - s) / L)
    cnt += x
    last_step = s + x * L
print(cnt)
