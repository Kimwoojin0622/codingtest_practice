def solution(my_string):
    result = 0
    for s in my_string:
        if s.isdigit():
            result = result + int(s)
    
    return result