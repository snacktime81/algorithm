def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left < right:
        l_v = people[left]
        r_v = people[right]

        s = l_v + r_v
        if (s > limit): # 두 사람의 몸무게의 합이 limit보다 크다면 몸무게가 큰 사람은 무조건 혼자서 타야한다.
            answer += 1
            right -= 1
        elif (s <= limit):
            answer += 1
            left += 1
            right -= 1
    if (left == right):
        answer += 1
    return answer