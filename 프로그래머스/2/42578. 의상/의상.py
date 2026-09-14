from collections import Counter
def solution(clothes):
    dicts = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in dicts:
            dicts[clothes[i][1]] = 1
        else:
            dicts[clothes[i][1]] += 1
    
    result = 1
    for data in dicts.values():
        result = result * (data + 1)
    
    return result - 1