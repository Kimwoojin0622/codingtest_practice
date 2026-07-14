def solution(x):
    st = str(x)
    
    tmp = 0
    for s in st:
        tmp += int(s)
    
    if x % tmp == 0:
        return True
    else:
        return False