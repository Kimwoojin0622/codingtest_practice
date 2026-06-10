def solution(my_string, index_list):
    result = []
    for n in index_list:
        result.append(my_string[n])
    
    return "".join(result)