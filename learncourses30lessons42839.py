from itertools import permutations


def find(num):
    check = [True] * (num + 1)
    check[0] = False
    check[1] = False

    for i in range(2, num + 1):
        if check[i]:
            tmp = 2
            while tmp * i <= num:
                check[i * tmp] = False
                tmp += 1
    return check


def solution(numbers):
    answer = 0
    nums = list(numbers)
    check = [False] * (10000000)

    arr = []

    for i in range(1, len(numbers) + 1):
        data = list(permutations(nums, i))
        for k in data:
            num = int(''.join(k))
            if not check[num]:
                arr.append(num)
                check[num] = True
    prime_check = find(max(arr))

    for i in arr:
        if (prime_check[i]):
            answer += 1
    return answer