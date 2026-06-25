def solution(n):
    temp, i, is_True = 1, 1, True
    
    while is_True:
        temp = temp * i
        if temp > n:
            result = i - 1
            is_True = False
        i = i + 1
    
    return result