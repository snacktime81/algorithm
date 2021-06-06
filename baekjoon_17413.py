#17413
import sys

S = sys.stdin.readline().strip()

word = []
k = False
count = 0

for i in S:
  if i == "<":
    if count > 0:
        word.reverse()
        print("".join(word), end="")
        del word[:]
        count = 0
        print("<", end="")
        k = True
    else:
      print("<", end="")
      k = True
    
  elif i == ">":
    print(">", end="")
    k = False
  else:
    if k:
      print(i, end="")
    elif k == False:
      if i == " " or i == "<":
        word.reverse()
        print("".join(word), end=" ")
        del word[:]
      else:
        word.append(i)
        count += 1
word.reverse()
print("".join(word))
