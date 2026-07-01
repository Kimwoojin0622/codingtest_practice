def solution(order):
    str_order = str(order)
    result = 0
    for s in str_order:
        if s == '3' or s == '6' or s == '9':
            result += 1
    
    return result