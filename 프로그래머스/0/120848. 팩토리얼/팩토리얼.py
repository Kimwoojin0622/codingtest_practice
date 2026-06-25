def solution(n):
    temp, i = 1, 1
    
    while True:
        temp = temp * i
        if temp > n:
            result = i - 1
            break
        i = i + 1
    
    return result
