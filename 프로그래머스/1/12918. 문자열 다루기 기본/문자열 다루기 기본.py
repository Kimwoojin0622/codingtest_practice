def solution(s):
    for data in s:
        tmp = ord(data)
        print(tmp)
        if tmp >= 65:
            return False
    
    # 길이 조건
    if len(s) == 4 or len(s) == 6:
        return True
    else:
        return False