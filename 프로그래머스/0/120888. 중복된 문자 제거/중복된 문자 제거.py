def solution(my_string):
    result = []
    for s in my_string:
        if s not in result:
            result.append(s)
        else:
            continue
    
    return "".join(result)