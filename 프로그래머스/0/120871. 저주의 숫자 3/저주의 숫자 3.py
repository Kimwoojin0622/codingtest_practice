def solution(n):
    tmp = 1
    result = []
    while len(result) < n:
        if tmp % 3 == 0 or '3' in str(tmp):
            tmp += 1
            continue
        else:
            result.append(tmp)
        tmp += 1
    
    return result[-1]
    
        
        
        
    
    # 1 2 3 4 5 6 7  8  9  10 11 12 13 14 15
    # 1 2 4 5 7 8 10 11 14 16 17 19 20 22 25 