def solution(numbers, n):
    i, result = 0, 0
    
    while i < len(numbers):
        result = result + numbers[i]
        if result > n:
            break
        i = i + 1
    
    return result