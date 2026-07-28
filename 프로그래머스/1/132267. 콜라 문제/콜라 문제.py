def solution(a, b, n):
    is_True = True
    coca, result = 0, 0
    
    while is_True:
        coca = (n // a) * b
        result += coca
        n = coca + (n % a)
        if n < a:
            is_True = False
    
    return result