def solution(l, r):
    result = []
    for num in range(l, r + 1):
        chk = str(num)
        chk = list(set(chk))
        chk.sort(reverse=True)
        
        
        if len(chk) == 1:
            if chk[0] == '5':
                result.append(num)
        else:
            if chk[0] == '5' and chk[1] == '0':
                result.append(num)
    
    if result:
        return result
    else:
        return [-1]
            