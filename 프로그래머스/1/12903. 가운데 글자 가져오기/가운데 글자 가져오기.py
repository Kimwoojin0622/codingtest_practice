def solution(s):
    if len(s) % 2 == 1:
        tmp = len(s) // 2 + 1
        return s[tmp - 1]
    else:
        tmp = len(s) // 2
        return s[tmp-1]+s[tmp]