def solution(before, after):
    before_list = [s for s in before]
    after_list = [s for s in after]
    
    before_list.sort()
    after_list.sort() # O(N log N)
    
    for i in range(len(before_list)):
        if before_list[i] != after_list[i]:
            return 0
    
    return 1