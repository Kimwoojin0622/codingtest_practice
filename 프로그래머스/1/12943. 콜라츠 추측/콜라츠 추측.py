def solution(n):
    tmp = 0
    while True:
        if n == 1:
            return tmp
        
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n * 3 + 1
        
        if tmp == 501:
            return -1
        
        tmp += 1