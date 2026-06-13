def solution(arr, queries):
    for data in queries:
        f_value, e_value = data[0], data[1]
        for i in range(f_value, e_value + 1):
            arr[i] += 1
    
    return arr
            