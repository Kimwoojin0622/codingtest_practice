def solution(my_string, queries):
    result = my_string
    for data in queries:
        f_value, e_value = data[0], data[1]
        temp = result[f_value : e_value + 1][::-1]
        result = result[:f_value] + temp + result[e_value + 1:]
    return result