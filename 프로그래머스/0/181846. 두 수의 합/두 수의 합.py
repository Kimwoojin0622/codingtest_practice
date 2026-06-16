def divide_i(i, tmp, length):
    if i == (length - 1):
        return str(tmp)
    else:
        return str(tmp % 10)

def solution(a, b):
    a, b = a[::-1], b[::-1]

    # a와 b중에 길이가 긴 것을 가져온다. 1234 + 56을 할 때, 1234 만큼 돌아야한다.
    length = max(len(a), len(b))
    result = []
    tmp, remain = 0, 0
    
    for i in range(length):
        if i > len(b) - 1:
            tmp = int(a[i]) + 0 + remain
            return_value = divide_i(i, tmp, length)
            result.append(return_value)
            remain = tmp // 10
        elif i > len(a) - 1:
            tmp = 0 + int(b[i]) + remain
            return_value = divide_i(i, tmp, length)
            result.append(return_value)
            remain = tmp // 10
        else:
            tmp = int(a[i]) + int(b[i]) + remain
            return_value = divide_i(i, tmp, length)
            result.append(return_value)
            remain = tmp // 10
    # 거꾸로된 result를 원래 상태로 만든다.
    result = result[::-1]
    return "".join(result)