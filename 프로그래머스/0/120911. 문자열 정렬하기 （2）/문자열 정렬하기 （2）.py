def solution(my_string):
    result = [s.lower() for s in my_string]
    result.sort()
    
    return "".join(result)