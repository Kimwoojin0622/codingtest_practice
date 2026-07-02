def solution(my_string):
    result = []
    for s in my_string:
        if s == s.upper():
            result.append(s.lower())
        else:
            result.append(s.upper())
    
    return "".join(result)