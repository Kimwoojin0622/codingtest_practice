def solution(myString, pat):
    result = ''
    for s in myString:
        if s == 'A':
            result += 'B'
        else:
            result += 'A'
            
    if pat in result:
        return 1
    else:
        return 0