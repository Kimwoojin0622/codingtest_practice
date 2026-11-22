def solution(s):
    length = len(s)
    if length % 2 == 0:
        tmp = length // 2
        return s[tmp-1 : tmp+1]
    else:
        tmp = length // 2
        return s[tmp]