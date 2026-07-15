def solution(numbers):
    result = 0
    for n in range(0, 10):
        if n not in numbers:
            result += n
    
    return result
    