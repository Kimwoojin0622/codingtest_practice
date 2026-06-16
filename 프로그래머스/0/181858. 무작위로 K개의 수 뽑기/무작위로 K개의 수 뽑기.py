def solution(arr, k):
    result = []
    for data in arr:
        if data not in result:
            result.append(data)
        if len(result) == k:
            break
    
    if len(result) < k:
        length = k - len(result)
        for _ in range(length):
            result.append(-1)
        return result
    else:
        return result