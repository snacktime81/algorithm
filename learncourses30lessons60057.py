def solution(s):
    m = [0 for i in range(len(s) + 1)]
    m[0] = int(1e9)
    for i in range(1, len(s) + 1):
        arr = []
        for j in range(0, len(s), i):
            arr.append(s[j:j + i])
        # print(arr)
        index = 0

        repeat = arr[index]
        cnt = 1

        for k in range(1, len(arr)):
            index += 1
            if (arr[k] == repeat):
                cnt += 1

            else:
                repeat = arr[k]
                if (cnt > 1):
                    m[i] += (len(str(cnt)) + i)
                else:
                    m[i] += i
                cnt = 1
        if (cnt > 1):
            m[i] += (len(str(cnt)) + i)
        else:
            m[i] += len(arr[-1])

    answer = min(m)
    return answer


def find(cnt):
    cnt_l = 0
    if (cnt == 1):
        cnt_l = 0
    elif cnt < 10:
        cnt_l = 1
    elif cnt < 100:
        cnt_l = 2
    elif cnt < 1000:
        cnt_l = 3
    else:
        cnt_l = 4
    return cnt_l


def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        key = ''
        cnt = 0
        l = 0
        for j in range(0, len(s), i):
            string = ''

            for k in range(j, j + i):  # 특정 길이 문자열 만들기
                if (k > len(s) - 1):
                    break
                string += s[k]
            # print(key ,string, cnt)
            if (key == string):
                cnt += 1
            else:
                if (cnt == 0):
                    cnt = 1
                elif (cnt > 1):
                    cnt_l = find(cnt)
                    l += cnt_l + len(key)
                else:
                    l += len(key)
                key = string
                cnt = 1

        l += find(cnt) + len(key)
        # print(i, l)
        answer = min(answer, l)

    return answer