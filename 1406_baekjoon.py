#1406
#time_over
import sys

word = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

im_k = len(word)
k = len(word)

for i in range(n):
  command = input()
  if command[0] == 'P':
    word = word[:k] + [command[2]] + word[k:]
    k += 1
  elif command == 'D':
    if not k == im_k:
      k += 1
  if not k == 0:
    if command == 'B':
      word = word[:k-1] + word[k:]
      k -= 1
    elif command == 'L':
      k -= 1
  else:
    continue

print("".join(word))
