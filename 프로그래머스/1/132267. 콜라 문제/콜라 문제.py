def solution(a, b, n):
    remain = 0
    result = 0
    
    while True:
        if n // a == 0:
            break
        remain = n % a
        result += (n//a) * b
        n = ((n // a) * b) + remain
    
    return result