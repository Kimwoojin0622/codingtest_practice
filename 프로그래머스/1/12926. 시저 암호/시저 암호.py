def solution(s, n):
    tmp = [st for st in s]

    for i in range(len(tmp)):
        if tmp[i] != " ":
            if ord(tmp[i]) <= 90 and ord(tmp[i]) >= 65:
                num = ord(tmp[i]) + n
                if num > 90:
                    num = num - 26
                tmp[i] = chr(num)
            elif ord(tmp[i]) <= 122 and ord(tmp[i]) >= 97:
                num = ord(tmp[i]) + n
                if num > 122:
                    num = num - 26
                tmp[i] = chr(num)
    return "".join(tmp)