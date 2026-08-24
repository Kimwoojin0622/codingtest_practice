from collections import deque
def solution(s):
    # O(N^2) 불가
    str_list = deque([st for st in s])
    
    tmp = []
    while len(str_list) != 0:
        if len(tmp) < 2:
            x = str_list.popleft()
            tmp.append(x)
            continue
            
        if len(tmp) >= 2:
            if tmp[-1] == tmp[-2]:
                tmp.pop()
                tmp.pop()
            else:
                x = str_list.popleft()
                tmp.append(x)
        
        if len(tmp) == len(s):
            break

    if len(tmp) == 2:
        if tmp[-1] == tmp[-2]:
            return 1
        else:
            return 0
    else:
        return 0