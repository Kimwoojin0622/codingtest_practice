from collections import deque
def solution(s):
    # O(N^2) 가능
    count = 0
    str_list = deque([st for st in s])
    
    same_list = []
    another_list = []
    while len(str_list) != 0:
        # same_list가 비어있을 때, 처음 x 값을 집어넣는다.
        if not same_list:
            value = str_list.popleft()
            same_list.append(value)
            continue
            
        if str_list[0] == same_list[0]:
            value = str_list.popleft()
            same_list.append(value)
            continue
        else:
            value = str_list.popleft()
            another_list.append(value)
        
        if len(same_list) == len(another_list):
            count += 1
            same_list = []
            another_list = []
        
    if not same_list:
        return count
    else:
        return count + 1