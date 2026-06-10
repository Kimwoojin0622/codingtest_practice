def solution(a, d, included):
    result = 0
    for boo in included:
        if boo == True:
            result = result + a
        a = a + d
    
    return result
    
    