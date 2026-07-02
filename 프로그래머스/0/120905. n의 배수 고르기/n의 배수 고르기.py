def solution(n, numlist):
    result = []
    
    for data in numlist:
        if data % n == 0:
            result.append(data)
    
    return result