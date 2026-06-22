def solution(rsp):
    result = []
    for data in rsp:
        if data == '0':
            result.append("5")
        elif data == '2':
            result.append("0")
        else:
            result.append("2")
    
    return "".join(result)