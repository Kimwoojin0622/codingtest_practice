def solution(n):
    n, result = str(n), 0
    
    for data in n:
        result += int(data)
    
    return result