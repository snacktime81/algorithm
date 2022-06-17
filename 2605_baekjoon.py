import sys;

n = int(sys.stdin.readline())
li = []
t = list(map(int, sys.stdin.readline().split()))
num = 1;
for i in t:
    li.insert(num-1-i, num)
    num += 1

for i in li:
    print(i, end=' ')