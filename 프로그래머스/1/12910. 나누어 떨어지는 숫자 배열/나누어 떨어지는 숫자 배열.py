def solution(arr, divisor):
    tmp = []
    for a in arr:
        if a % divisor == 0:
            tmp.append(a)
    
    if not tmp:
        return [-1]
    else:
        result = sorted(tmp)
        return result
    