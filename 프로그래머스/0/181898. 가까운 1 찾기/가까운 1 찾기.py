def solution(arr, idx):
    result = []
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            result.append(i)
    
    if result:
        return min(result)
    else:
        return -1