#1406
#time_over
import sys

word = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

im_k = len(word)
k = len(word)

for i in range(n):
  command = list(sys.stdin.readline().strip())
  if command[0] == 'P':
    word.insert(k , command[2])
    k += 1
  elif command[0] == 'D':
    if not k == im_k:
      k += 1
  
  if not k == 0:
    if command[0] == 'B':
      del word[k-1]
      k -= 1
    elif command[0] == 'L':
      k -= 1
  else:
    continue

print("".join(word))
