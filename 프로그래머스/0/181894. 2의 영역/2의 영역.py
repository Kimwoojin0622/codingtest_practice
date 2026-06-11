def solution(arr):
    idx_list = []
    for i in range(len(arr)):
        if arr[i] == 2:
            idx_list.append(i)
    
    if idx_list:
        min_value = min(idx_list)
        max_value = max(idx_list)
        return arr[min_value : max_value + 1]
    else:
        return [-1]