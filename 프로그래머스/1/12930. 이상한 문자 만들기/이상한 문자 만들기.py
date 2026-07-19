def solution(s):
    i, chk = 0, 0
    result = []
    while i < len(s):
        if s[i] == ' ':
            result.append(s[i])
            chk = 0
        elif chk % 2 == 0:
            result.append(s[i].upper())
            chk += 1
        else:
            result.append(s[i].lower())
            chk += 1
        i += 1
    
    return "".join(result)
