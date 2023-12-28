def solution(k, tangerine):
    arr = dict()
    for i in tangerine:
        try:
            arr[i] += 1
        except:
            arr[i] = 1
    costs = []
    for i in arr:
        costs.append(arr[i])
    costs.sort(reverse=True)
    answer = 0
    for cost in costs:
        k -= cost
        answer += 1
        if(k <= 0):
            break
    return answer