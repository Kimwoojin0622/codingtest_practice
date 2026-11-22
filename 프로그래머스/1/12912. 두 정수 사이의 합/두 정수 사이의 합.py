def solution(a, b):
    value = []
    result = 0
    if a == b:
        return a
    elif a < b:
        for i in range(a, b+1):
            value.append(i) 
        for v in value:
            result += v
    else:
        for i in range(b, a+1):
            value.append(i)
        for v in value:
            result += v
    
    return result
            