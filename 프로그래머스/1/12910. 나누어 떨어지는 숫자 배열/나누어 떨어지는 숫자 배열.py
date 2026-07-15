def solution(arr, divisor):
    result = []
    for n in arr:
        if n % divisor == 0:
            result.append(n)
    
    if result:
        result.sort()
        return result
    else:
        return [-1]