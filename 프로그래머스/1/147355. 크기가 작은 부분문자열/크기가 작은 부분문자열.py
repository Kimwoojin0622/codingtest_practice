def solution(t, p):
    result, length = 0, len(p)
    
    for i in range(0, len(t) - length + 1):
        value = int(t[i:i+length])
        if value <= int(p):
            result += 1
    
    return result