#1003

T = int(input())
for _ in range(T):
  li = [{0:1, 1:0}, {0:0, 1:1}, {0:1, 1:1}]
  n = int(input())
  for i in range(3, n+1):
    li.append({0:li[i-1][0]+li[i-2][0], 1:li[i-1][1] + li[i-2][1]})
  print(li[n][0], li[n][1])