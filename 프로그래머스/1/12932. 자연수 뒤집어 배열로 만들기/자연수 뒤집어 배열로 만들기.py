def solution(n):
    st = str(n)
    value = []
    for s in st:
        value.append(s)
    
    result = value[::-1]
    for i in range(len(result)):
        result[i] = int(result[i])
    
    return result