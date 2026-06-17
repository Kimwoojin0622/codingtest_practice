def solution(str_list, ex):
    result = ''
    for data in str_list:
        if ex not in data:
            result = result + data
    
    return result