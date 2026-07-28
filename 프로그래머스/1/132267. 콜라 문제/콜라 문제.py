def solution(a, b, n):
    result = []
    is_True = True
    coca = 0
    while is_True:
        coca = (n // a) * b
        result.append(coca)
        n = coca + (n % a)
        if n < a:
            is_True = False
    
    return sum(result)