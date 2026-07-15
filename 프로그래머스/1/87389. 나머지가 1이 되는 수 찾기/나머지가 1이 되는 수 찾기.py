def solution(n):
    min_temp = 1000001
    for i in range(1, n):
        if n % i == 1:
            if i < min_temp:
                min_temp = i
    
    return min_temp