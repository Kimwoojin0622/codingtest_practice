def solution(num_list):
    multiple_values, multiple_plus_values = 1, 0
    for n in num_list:
        multiple_values *= n
        multiple_plus_values += n
        
    if multiple_values < multiple_plus_values ** 2:
        return 1
    else:
        return 0