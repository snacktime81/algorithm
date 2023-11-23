#https://www.acmicpc.net/problem/1043

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 총 사람수, 총 파티수

def find(parent, target):
    if( parent[target] != target):
        parent[target] = find(parent, parent[target])
    return parent[target]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if( a < b ):
        parent[b] = a
    else:
        parent[a] = b

truth = list(map(int, input().split())) 
truth_cnt = truth[0]

parent = [i for i in range(n+1)]
        
if (truth_cnt == 0): 
    truth_people_list = [] # 진실을 아는 사람이 0명
else:
    truth_people_list = truth[1:] # 진실을 아는 사람의 리스트

party_sets = [] # 파티들의 집합
    
for _ in range(m):
    line = list(map(int, input().split()))
    party_people = line[1:] # 파티에 참여한 사람들
    
    party_sets.append(party_people)
    
    for i in party_people: # parent에 같이 이야기를 듣는 사람들을 선별
        for j in party_people:
            union(parent, i, j)

for party in party_sets: # 마저 연결되지 않은 값들을 연결
    for i in party: 
        for j in party:
            union(parent, i, j)
    
for i in range(truth_cnt):
    truth_people_list[i] = parent[truth_people_list[i]] # 진실을 아는 사람들을 parent 값으로 변경
    
cnt = 0

print("parent: ", parent)
print('truth: ', truth_people_list)

for party in party_sets:
    for person in party:
        if parent[person] in truth_people_list:
            cnt += 1
            break
        

print(m-cnt)

