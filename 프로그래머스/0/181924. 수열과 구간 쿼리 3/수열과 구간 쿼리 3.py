def solution(arr, queries):
    for data in queries:
        f_value, e_value = data[0], data[1]
        # print(f_value, e_value)
        temp = arr[f_value]
        arr[f_value] = arr[e_value]
        arr[e_value] = temp
        # print(arr)
    
    return arr