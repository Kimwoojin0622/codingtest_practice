def solution(s):
    # 0 P의 개수, 1 Y의 개수
    result = [0, 0]
    for data in s:
        if data.lower() == 'p':
            result[0] += 1
        elif data.lower() == 'y':
            result[1] += 1
    
    if result[0] == result[1]:
        return True
    else:
        return False