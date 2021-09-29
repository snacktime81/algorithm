#1269
import sys
n, m = map(int, sys.stdin.readline().split())
first_list = set(map(int, sys.stdin.readline().split()))
second_list = set(map(int, sys.stdin.readline().split()))

a = len(first_list - second_list)
b = len(second_list - first_list)
print(a+b)