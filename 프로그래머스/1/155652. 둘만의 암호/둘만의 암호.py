def solution(s, skip, index):
    # ord('a') = 97
    # ord('z') = 122
    result = ''
    
    for st in s:
        tmp = ord(st)
        i = 1
        li = []
        for _ in range(1, index + 1):
            is_True = True
            while is_True:
                if ord(chr(tmp + i)) > ord('z'):
                    tmp = ord('a')
                    i = 0
                    
                if chr(tmp + i) not in skip:
                    is_True = False
                    li.append(chr(tmp + i))
                    i = i + 1 
                else:
                    i = i + 1
        result = result + li[-1]
        
    return result         