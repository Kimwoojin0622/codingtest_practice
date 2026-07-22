def solution(s, n):
    # ord(a)는 97, ord(A)는 65
    # ord(z)는 122, ord(Z)는 90
    
    result = []
    for data in s:
        if 65 <= ord(data) <= 90:
            tmp = ord(data) + n
            if tmp > 90:
                tmp = tmp - 26
                result.append(chr(tmp))
            else:
                result.append(chr(tmp))
        elif 97 <= ord(data) <= 122:
            tmp = ord(data) + n
            if tmp > 122:
                tmp = tmp - 26
                result.append(chr(tmp))
            else:
                result.append(chr(tmp))
        else:
            result.append(data)
    
    return "".join(result)
