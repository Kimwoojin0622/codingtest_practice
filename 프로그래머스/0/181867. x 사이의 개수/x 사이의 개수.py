def solution(myString):
    str_list = list(myString.split("x"))
    
    result = []
    for s in str_list:
        result.append(len(s))
    
    return result