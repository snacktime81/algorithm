from itertools import permutations
from collections import deque
move = [(-9, -3, -1), (-9, -1, -3), (-3, -9, -1), (-3, -1, -9), (-1, -9, -3), (-1, -3, -9)]
#move = [-9, -3, -1]

def right(arr):
    while len(arr) < 3:
        arr.append(0)

N = int(input())
SCVS = list(map(int, input().split()))
right(SCVS)
#m = list(permutations(move, N))

dp = [[[1e9 for _ in range(61)] for _ in range(61)] for _ in range(61)] 

# dp = []

# for i in range(N):
#     arr = [0 for _ in range(61)]
#     dp.append(arr)

# if N == 1:
#     dp[SCVS[0]] = 0
# elif N == 2:
#     dp[SCVS[0]][SCVS[1]] = 0
# else:
#     dp[SCVS[0]][SCVS[1]][SCVS[2]] = 0
dp[SCVS[0]][SCVS[1]][SCVS[2]] = 0
q = deque([(SCVS, 0)])

while q:
    scvs, cnt = q.popleft()
    a, b, c = scvs
    
    if(sum(scvs) == 0):
        print(cnt)
        break
    
    for i in move:
        a = scvs[0] + i[0]
        b = scvs[1] + i[1]
        c = scvs[2] + i[2]
        
        a = a if a >= 0 else 0
        b = b if b >= 0 else 0
        c = c if c >= 0 else 0
        
        d = [a, b, c]
        if(dp[a][b][c] > cnt+1):
            q.append([d, cnt+1])
            dp[a][b][c] = cnt+1
