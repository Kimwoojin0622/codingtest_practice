def solution(array):
    result = 0
    for data in array:
        tmp = str(data)
        result = result + tmp.count("7")
    
    return result