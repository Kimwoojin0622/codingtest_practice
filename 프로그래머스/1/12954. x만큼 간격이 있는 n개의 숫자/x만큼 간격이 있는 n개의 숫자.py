def solution(x, n):
    result = []
    if x > 0:
        for i in range(x, x*n+1, x):
            result.append(i)
    elif x < 0:
        for i in range(x, x*n-1, x):
            result.append(i)
    else:
        return [0] * n
    
    return result
        