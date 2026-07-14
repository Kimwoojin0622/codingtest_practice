def solution(n):
    stN = str(n)
    tmp = [int(s) for s in stN]
    tmp.sort(reverse=True)
    
    result = ''
    for s in tmp:
        t = str(s)
        result += t
    
    return int(result)