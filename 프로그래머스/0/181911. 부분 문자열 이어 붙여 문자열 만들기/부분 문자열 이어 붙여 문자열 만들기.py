def solution(my_strings, parts):
    result = []
    for i in range(len(my_strings)):
        data = my_strings[i]
        s = data[parts[i][0] : parts[i][1] + 1]
        result.append(s)
        
    return "".join(result)
        