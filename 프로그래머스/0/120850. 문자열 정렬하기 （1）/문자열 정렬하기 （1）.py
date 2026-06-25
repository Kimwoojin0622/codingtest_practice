def solution(my_string):
    result = [int(s) for s in my_string if s.isdigit()]
    result.sort()
    
    return result
