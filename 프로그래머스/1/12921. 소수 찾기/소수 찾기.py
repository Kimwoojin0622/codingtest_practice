def solution(n):
    is_decimal = [True] * (n + 1)
    is_decimal[0], is_decimal[1] = False, False
    
    for i in range(2, n + 1):
        if is_decimal[i] == True:
            for j in range(i * 2, n + 1, i):
                is_decimal[j] = False
    
    return sum(is_decimal)