def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        result = 1
        for n in num_list:
            result = result * n
        
        return result