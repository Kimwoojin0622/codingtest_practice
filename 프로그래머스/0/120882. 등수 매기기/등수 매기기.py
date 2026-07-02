def solution(score):
    avg_list = [sum(data) / 2 for data in score]
    sorted_list = sorted(avg_list, reverse = True)
    
    result = {}
    for i, z in enumerate(sorted_list):
        if z not in result:
            result[z] = i + 1

    i = 0
    for data in avg_list:
        for it in result.items():
            if it[0] == data:
                avg_list[i] = it[1]
                i = i + 1
    
    return avg_list
    
    
                
