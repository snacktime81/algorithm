#11729
import sys

n = int(sys.stdin.readline())

#from_pos 시작, aux_pos 보조, to_pos 도착

def hanoi(n, from_pos, aux_pos, to_pos):
  if n == 1:
    print(from_pos, to_pos)
    return
  hanoi(n-1, from_pos, to_pos, aux_pos)
  print(f"{from_pos} {to_pos}")
  hanoi(n-1, aux_pos, from_pos, to_pos)


print(2**n-1)
hanoi(n, 1, 2, 3)