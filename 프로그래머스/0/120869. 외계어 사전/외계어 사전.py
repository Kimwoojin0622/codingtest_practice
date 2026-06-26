def solution(spell, dic):

    for data in dic:
        temp_set = set([s for s in data])
        length, tmp = len(temp_set), 0
        # print(temp_set)
        for chk in temp_set:
            if chk in spell:
                tmp += 1
                # print(tmp, length)
        
        if tmp == length and tmp == len(spell):
            return 1
        
    return 2
        