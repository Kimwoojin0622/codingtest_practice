from collections import deque
def solution(people, limit):
    sp = sorted(people)
    i, j = 0, len(sp) - 1
    boats = 0
    
    while True:
        if i == j:
            boats += 1
            break
        elif i > j:
            break
            
        if sp[i] + sp[j] > limit:
            boats += 1
        else:
            boats += 1
            i += 1
        j -= 1
            
    return boats