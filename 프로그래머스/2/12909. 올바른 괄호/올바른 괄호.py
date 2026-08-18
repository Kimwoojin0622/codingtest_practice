def solution(s):
    tmp = []
    for data in s:
        tmp.append(data)
        if len(tmp) > 1:
            if tmp[-2] + tmp[-1] == '()':
                tmp.pop()
                tmp.pop()
                
    if len(tmp) == 0:
        return True
    else:
        return False