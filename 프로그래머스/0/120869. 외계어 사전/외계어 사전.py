def solution(spell, dic):

    for data in dic:
        temp_set = set([s for s in data])
        length, tmp = len(temp_set), 0

        for chk in temp_set:
            if chk in spell:
                tmp += 1
        
        if tmp == length and tmp == len(spell):
            return 1
        
    return 2
