def solution(arr, k):
    result = []
    for data in arr:
        if data not in result:
            result.append(data)
        if len(result) == k:
            break
    
    if len(result) < k:
        # 완성된 배열의 길이가 k보다 작을 시, result 리스트에 -1 원소 추가
        length = k - len(result)
        for _ in range(length):
            result.append(-1)
        return result
    else:
        return result
