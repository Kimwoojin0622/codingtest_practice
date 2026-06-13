def solution(my_string, m, c):
    result = []
    for i in range(c - 1, len(my_string), m):
        result.append(my_string[i])
    
    return "".join(result)