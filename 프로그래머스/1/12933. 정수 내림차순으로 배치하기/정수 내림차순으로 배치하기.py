def solution(n):
    # n 8000000000
    
    st = str(n)
    value = []
    for s in st:
        value.append(s)
    
    tmp_list = sorted(value, reverse=True)
    
    result = ''
    for t in tmp_list:
        result += t
    
    return int(result)