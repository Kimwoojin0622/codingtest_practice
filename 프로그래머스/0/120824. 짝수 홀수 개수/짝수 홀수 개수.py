def solution(num_list):
    result = [0, 0] # [짝수, 홀수]
    
    for num in num_list:
        if num % 2 == 0:
            result[0] += 1
        else:
            result[1] += 1
    
    return result