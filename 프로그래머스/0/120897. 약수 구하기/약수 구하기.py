def solution(n):
    result = set()
    
    for i in range(1, n + 1):
        if n % i == 0:
            result.add(i)
    
    result_list = list(result)
    result_list.sort()
    
    return result_list