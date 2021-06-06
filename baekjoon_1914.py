import sys

#from 시작
#to 도착
#aux 보조

def hanoi(n, from_pos, aux_pos, to_pos):
  if n == 1:
    print(from_pos, to_pos)
    return
  hanoi((n-1), from_pos, to_pos, aux_pos)
  print(from_pos, to_pos)
  hanoi((n-1), aux_pos, from_pos, to_pos)


n = int(sys.stdin.readline())
li = [0 for _ in range(n+1)]
for i in range(n+1):
  if i == 1:
    li[1] = 1
  else:
    li[i] = li[i-1]*2 + 1

if n <= 20:
  print(li[n])
  hanoi(n, 1, 2, 3)
else:
  print(li[n])

