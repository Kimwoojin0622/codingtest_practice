def solution(n):
    tmp = n // 2
    
    for i in range(1, tmp + 1):
        if i * i == n:
            return 1
    
    return 2
    
    