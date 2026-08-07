def solution(n, m, section):
    result = 0
    painted = 0
    
    for sec in section:
        if sec > painted:
            result += 1
            painted = sec + m - 1
    
    return result
        