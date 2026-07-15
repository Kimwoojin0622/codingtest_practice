def solution(n):
    count = 0
    
    if n == 1:
        return count
    else:
        is_True = True
        while count < 500:
            if n % 2 == 0:
                n = n // 2
            elif n % 2 == 1:
                n = n * 3 + 1
            
            count += 1
            if n == 1 and count <= 500:
                is_True = False
                return count
            if n != 1 and count == 500:
                return -1
        