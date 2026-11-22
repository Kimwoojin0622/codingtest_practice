def solution(s):
    chk = {'p':0, 'y':0}
    
    s = s.lower()
    for data in s:
        if data == 'p' or data == 'y':
            chk[data] += 1
    
    if chk['p'] == chk['y']:
        return True
    else:
        return False