def solution(intStrs, k, s, l):
    result = []
    length = s + l
    
    for data in intStrs:
        temp = data[s : length]
        if int(temp) > k:
            result.append(int(temp))
    
    return result