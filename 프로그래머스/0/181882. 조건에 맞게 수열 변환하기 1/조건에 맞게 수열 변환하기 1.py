def solution(arr):
    result = []
    for n in arr:
        if n >= 50 and n % 2 == 0:
            result.append(n // 2)
        elif n < 50 and n % 2 != 0:
            result.append(n * 2)
        else:
            result.append(n)
            
    return result