def solution(s):
    result = []
    for data in s:
        if s.count(data) == 1:
            result.append(data)
    
    result.sort()
    return "".join(result)