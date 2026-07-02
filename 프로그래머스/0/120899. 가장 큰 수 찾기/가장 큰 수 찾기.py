def solution(array):
    max_value = max(array)
    result = [max_value, array.index(max_value)]
    
    return result